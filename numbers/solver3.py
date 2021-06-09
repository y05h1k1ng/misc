data = 252376267032144643086459111951520584928729531351758542982596669174477589710286198885748394640283226071880324906312217455275419657943435199787316315643337252381879508966893673637624796814941

def get_digit(x):
    res = 0
    while x:
        x //= 10
        res += 1
    return res

MAX_NUM = 99
LEN = get_digit(data)

visited = [[False]*MAX_NUM for _ in range(LEN+1)] # visited[LEN+1][MAX_NUM]
ans = []

def f(i, digit):
    #print(f"[*] {i = }, {digit = }")
    if i == LEN:
        if all(visited[i]):
            return True
        else:
            return False
    if i + digit > LEN:
        return False
    #if data[i] == "0":
    #    return False
    
    num = (data // (10**(LEN-(i+digit)))) % (10**digit)
    #print(f"    {num = }")
    if get_digit(num) != digit:
        return False
    if num > MAX_NUM:
        return False
    if visited[i][num-1]:
        return False

    for idx in range(MAX_NUM):
        visited[i+digit][idx] = visited[i][idx]
    visited[i+digit][num-1] = True
    #print(f"    {list(map(int, visited[i+digit]))}")
    
    if f(i+digit, 1):
        ans.append(num)
        return True
    if f(i+digit, 2):
        ans.append(num)
        return True

if f(0, 1):
    print(ans[::-1])
elif f(0, 2):
    print(ans[::-1])
