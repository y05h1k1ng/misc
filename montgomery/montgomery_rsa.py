from montgomery import MR
from Crypto.Util.number import getPrime, inverse
from random import getrandbits

u = -(2**62 + 2**55 + 1)
N = 36*pow(u, 4) + 36*pow(u, 3) + 24*pow(u, 2) + 6*u + 1

n = 0xfffffffffffffffffffffffffffffffeffffffffffffffff
c = 5003436851221201713926160155297504393934861937006144945855291451476606451598 # MR(C)
d = 0xdf3165e9

one = MR(256, n, 32).num_to_MR(1)
print(one.T)
C = MR(256, n, 32)
C.T = c
M = C.pow(d)

print(hex(M.T))
exit()

for _ in range(10):
    d = getPrime(32)
    e = inverse(d, N-1)

    m = getrandbits(32)
    M = MR(256, N, 128).num_to_MR(m)
    C = M.pow(e)
    print(m == C.pow(d).MR_to_num())
