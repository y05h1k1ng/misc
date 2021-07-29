from montgomery import MR
from Crypto.Util.number import getPrime, inverse
from random import getrandbits
from time import time

def check():
    u = -(2**62 + 2**55 + 1)
    N = 36*pow(u, 4) + 36*pow(u, 3) + 24*pow(u, 2) + 6*u + 1

    for _ in range(10):
        d = getPrime(32)
        e = inverse(d, N-1)

        m = getrandbits(32)
        M = MR(256, N, 128).num_to_MR(m)
        C = M.pow(e)
        print(m == C.pow(d).MR_to_num())
    return

def example():
    n = 0xfffffffffffffffffffffffffffffffeffffffffffffffff
    c = 5003436851221201713926160155297504393934861937006144945855291451476606451598 # MR(C)
    d = 0xdf3165e9

    one = MR(256, n, 32).num_to_MR(1)
    print(one.T)
    C = MR(256, n, 32)
    C.T = c
    M = C.pow(d)

    print(hex(M.T))
    return

def speed():
    u = -(2**62 + 2**55 + 1)
    N = 36*pow(u, 4) + 36*pow(u, 3) + 24*pow(u, 2) + 6*u + 1

    ai = [getrandbits(128) for _ in range(100)]
    bi = [getrandbits(128) for _ in range(100)]

    print("========== multiplication(a*b % n) ==========")
    print("[+] build-in")
    start = time()
    for a, b in zip(ai, bi):
        _ = (a * b) % N
    print("    time:", time() - start)
    print("[+] montgomery")
    start = time()
    for a, b in zip(ai, bi):
        x = MR(256, N).num_to_MR(a) * MR(256, N).num_to_MR(b)
        _ = x.MR_to_num()
    print("    time:", time() - start)

    print()
    print("========== exponentiation(a^b % n) ==========")
    print("[+] build-in")
    start = time()
    for a, b in zip(ai, bi):
        _ = pow(a, b, N)
    print("    time:", time() - start)
    print("[+] montgomery")
    start = time()
    for a, b in zip(ai, bi):
        X = MR(256, N).num_to_MR(a)
        x = X.pow(b)
        _ = x.MR_to_num()
    print("    time:", time() - start)

if __name__=="__main__":
    speed()
