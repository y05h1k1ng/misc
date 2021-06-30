from decimal import Decimal, getcontext
from Crypto.Util.number import isPrime

getcontext().prec = 52

sqrt2 = Decimal(2).sqrt()
print(sqrt2)

s_dec = str(sqrt2).split(".")[1]
for i in range(50-11):
    if s_dec[i] == "0":
        continue
    num = int(s_dec[i:i+11])
    if isPrime(num):
        print(num)
