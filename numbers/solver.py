with open("sample3/input3.txt") as f:
    data = f.read().strip()

#data = "252376267032144643086459111951520584928729531351758542982596669174477589710286198885748394640283226071880324906312217455275419657943435199787316315643337252381879508966893673637624796814941"

def f(s, ans):
    #print(s)
    if s == data:
        print(ans)
        return
    for i in range(1, 100):
        if i in ans:
            continue
        if data.startswith(s + str(i)):
            f(s + str(i), ans[:] + [i])

f("", [])
