class MR:
    def __init__(self, R_bits, N, k=None):
        self.R_bits = R_bits
        self.R = 2**R_bits
        self.R_2 = self.R ** 2
        self.N = N
        self.N_inv = self.inv(N, self.R)
        self.T = -1
        
        # parameters of k bit Montgomery multiplication
        if k is None:
            self.k = R_bits
        else:
            assert R_bits % k == 0
            self.k = k
        self.block_num = R_bits // self.k
        self.Q = 2**self.k
        
    def __mul__(self, B):
        res = MR(self.R_bits, self.N, self.k)
        res.T = self.MR(self.T, B.T)
        return res

    def num_to_MR(self, num):
        self.T = self.MR(num, self.R_2 % self.N)
        return self

    def MR_to_num(self):
        return self.MR(self.T, 1)

    def MR(self, A:int, B:int, debug=False):
        # k bit Montgomery multiplication
        if debug:
            print(f"[*] {A = :#x}")
            print(f"[*] {B = :#x}")
        S = 0
        for i in range(self.block_num):
            bi = (B >> (self.k*i)) & (self.Q-1)
            q = (((S + bi*A) & (self.Q-1)) * self.N_inv) & (self.Q-1)
            S = (S + q*self.N + bi*A) >> self.k
            if debug:
                print(f"[*] block {i}/{self.block_num}")
                print(f"    {bi = :#x}")
                print(f"    {q = :#x}")
                print(f"    {S = :#x}")
        return S

    def pow(self, k:int):
        # left binary method
        res = self
        bits = bin(k)[3:]
        for bit in bits:
            res = res * res
            if int(bit):
                res = res * self
            
        return res
        
    def inv(self, N, R):
        # n * n' = -1 (mod R)
        t = 0
        res = 0
        i = 1
        while R > 1 :
            if not (t & 1):
                t += N
                res += i
            i <<= 1
            t >>= 1
            R >>= 1
        return res

if __name__=="__main__":
    u = -(2**62 + 2**55 + 1)
    N = 36*pow(u, 4) + 36*pow(u, 3) + 24*pow(u, 2) + 6*u + 1

    print(hex(MR(256, N, 32).MR(2, 3, debug=True)))
    exit()

    A = MR(256, N, 128).num_to_MR(2)
    B = MR(256, N, 128).num_to_MR(3)
    C = A * B
    c = C.MR_to_num()

    print(f"{A.T = :#x}")
    print(f"{B.T = :#x}")
    print(f"{C.T = :#x}")
    print(f"{c = :#x}\n")

    X = A.pow(40710)
    print(hex(X.MR_to_num()))
