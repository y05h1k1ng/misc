from collections import deque, defaultdict

data = "252376267032144643086459111951520584928729531351758542982596669174477589710286198885748394640283226071880324906312217455275419657943435199787316315643337252381879508966893673637624796814941"

LEN = len(data)

que = deque([])
visited = defaultdict(list)

que.append((0, 1, ""))
que.append((0, 2, ""))

while len(que):
    i, digit, parent = que.popleft()
    
    if "".join(visited[parent]) == data:
        break
    if i + digit > LEN:
        continue
    
    num = data[i:i+digit]
    if num[0] == "0":
        continue
    if num in visited[parent]:
        continue
    visited[num] = visited[parent] + [num]
    if digit == 2:
        del visited[parent]

    que.append((i+digit, 1, num))
    que.append((i+digit, 2, num))

print(visited)
