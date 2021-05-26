def one(n):
    res = []
    for i in range(1, n+1):
        if i % 15 == 0:
            res.append("FB")
        elif i % 5 == 0:
            res.append("B")
        elif i % 3 == 0:
            res.append("F")
        else:
            res.append(i)
    return res

def two(n):
    res = []
    for i in range(1, n+1):
        if i // 15 == i / 15:
            res.append("FB")
        elif i // 5 == i / 5:
            res.append("B")
        elif i // 3 == i / 3:
            res.append("F")
        else:
            res.append(i)
    return res

def three(n):
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
    return res

def four(n):
    return ["FB" if i%15 == 0 else "B" if i%5 == 0 else "F" if i%3 == 0 else i for i in range(1, n + 1)]

def five(n):
    return list(map(lambda i:"FB" if i/15 == i//15 else "B" if i/5 == i//5 else "F" if i/3 == i//3 else i, range(1, n + 1)))

max_n = 100
funcs = [one, two, three, four, five]
for n in range(1, max_n + 1):
    if len(set(map(str, [f(n) for f in funcs]))) == 1:
        print(f"[+] {n = }: Correct")
    else:
        print(f"[-] {n = }: Wrong:(")
