import sys

def is_prime(x):
    # 愚直に実装
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def is_prime_sqrt(x):
    # 最大の素因数は sqrt(n) 以下
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

def fermat(a, x):
    if x % a == 0:
        return False

    if pow(a, x-1, x) != 1: # O(logn) https://maspypy.com/%E6%95%B0%E5%AD%A6-n%E4%B9%97%E3%81%AE%E8%A8%88%E7%AE%97
        return False
    return True

def is_prime_fermat(x):
    primes = [2, 3, 5, 7, 11]
    if x in primes:
        return True

    # 擬素数を含む
    for p in primes:
        if not fermat(p, x):
            return False
    return True

def eratosthenes(n):
    # エラトステネスのふるい
    nums = set(range(2, n+1))
    primes = []

    p = min(nums)
    nums.remove(p)
    primes.append(p)
    
    while p * p <= n:
        rm = set()
        for num in nums:
            if num % p == 0:
                rm.add(num)
        nums -= rm
        
        p = min(nums)
        nums.remove(p)
        primes.append(p)
    
    return primes + list(nums)

def faster_eratosthenes(n):
    primes = []
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, n+1):
        if is_prime[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                is_prime[j] = False
    return primes

# 2 ~ n までの素数を列挙
n = int(sys.argv[1])

if n < 2:
    print("[-] oops, didn't satisfy n >= 2")
    exit()

if len(sys.argv) == 3:
    debug = True
else:
    debug = False

res = [list() for _ in range(4)]
for i in range(2, n+1):
    if is_prime(i): # O(n^2)
        res[0].append(i)
    if is_prime_sqrt(i): # O(n*sqrt(n))
        res[1].append(i)
    if is_prime_fermat(i): # O(n*logn) ?
        res[2].append(i)

res[3] = eratosthenes(n) # O(n*loglogn)

if debug:
    for r in res:
        print("[*]", r)

if len(res[2]) != len(res[3]):
    print()
    print("[-] fermat pseudoprime")
    print(set(res[2]) - set(res[3]))
