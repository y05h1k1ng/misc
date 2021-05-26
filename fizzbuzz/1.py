# 問1: 制限なし
n = int(input("n : "))

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

print(res)
