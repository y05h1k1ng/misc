def square_and_multiply(a, k):
    # 左バイナリ法
    # z = a^k
    A = a
    R = a
    for i in range(k.bit_length() - 2, -1, -1):
        A *= A
        if (k >> i) & 1:
            A *= R
    return A

def square_and_multiply_always(a, k):
    R = [a] * 3
    for i in range(k.bit_length() - 2, -1, -1):
        R[1] *= R[1]
        b = (k >> i) & 1
        R[b] *= R[2]
    return R[1]

def radix(T, x):
    # return (T)x
    assert x <= 10, "[-] not implemented"
    res = []
    while T:
        k = T % x
        T = T // x
        res.append(k)
    return res[::-1]

def m_ary_exponentiation(a, k):
    # return a^k
    m = 8 # m進数
    R = [a]
    m_digits = radix(k, m) # (k)m
    for i in range(m-2):
        R.append(R[i] * a)
    # print(f"{m_digits = }")
    # print(f"{R = }")
    d = m_digits[0]
    A = R[d-1]
    for i in range(1, len(m_digits)):
        A = pow(A, m)
        d = m_digits[i]
        if d:
            A *= R[d-1]
    return A

def test(time):
    from random import getrandbits
    for _ in range(time):
        a = getrandbits(10)
        k = getrandbits(10)
        res1 = pow(a, k)
        res2 = square_and_multiply(a, k)
        res3 = square_and_multiply_always(a, k)
        res4 = m_ary_exponentiation(a, k)
        print(res1 == res2, res1 == res3, res1 == res4)

if __name__=="__main__":
    test(10)
