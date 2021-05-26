from montgomery import MR
from Crypto.Util.number import getPrime, inverse
from random import getrandbits

u = -(2**62 + 2**55 + 1)
N = 36*pow(u, 4) + 36*pow(u, 3) + 24*pow(u, 2) + 6*u + 1

for _ in range(10):
    d = getPrime(32)
    e = inverse(d, N-1)

    m = getrandbits(32)
    M = MR(256, N, 128).num_to_MR(m)
    C = M.pow(e)
    print(m == C.pow(d).MR_to_num())
