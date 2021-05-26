# 問2: 剰余演算子を利用しない
n = int(input("n : "))

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

print(res)
