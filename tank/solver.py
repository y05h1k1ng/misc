data = input()

LEN = len(data) + 1
tank = [0] * LEN
high = [0]
for i, x in enumerate(data):
    if x == "/":
        high.append(high[i]+1)
    elif x == "\\":
        high.append(high[i]-1)
    else:
        high.append(high[i])

for min_high in range(min(high), max(high)):
    cand = [False] * LEN
    for i in range(LEN):
        if min_high == high[i]:
            cand[i] = True

    comp = [cand[0]]
    for i in range(1, LEN):
        if cand[i-1] != cand[i]:
            comp.append(cand[i])

    comp[0] = False
    comp[-1] = False

    idx = 0
    flag = comp[idx]
    for i in range(1, LEN):
        if cand[i-1] != cand[i]:
            idx += 1
            flag = comp[idx]
        if cand[i] and flag:
            tank[i] += 1
            high[i] += 1

    for i in range(LEN):
        if min_high == high[i]:
            high[i] += 1

    # print("[*] high", high)
    # print("    tank", tank)
    # print("    cand", cand)
    # print("    comp", comp)

ans = sum(tank)
ans_list = []
for i in range(1, LEN):
    if tank[i-1] == 0 and tank[i]:
        ans_list.append(tank[i])
    elif tank[i]:
        ans_list[-1] += tank[i]
print(ans)
print(*ans_list)
