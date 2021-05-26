# 問3: map関数を利用する
n = int(input("n : "))

def fizzbuzz(x):
    if x % 15 == 0:
        return "FB"
    elif x % 5 == 0:
        return "B"
    elif x % 3 == 0:
        return "F"
    else:
        return x

res = list(map(fizzbuzz, range(1, n+1)))
print(res)
