from utils import show_graph, Timer
import sys

sys.setrecursionlimit(10**6)

debug = True
N = int(input("N = "))
#N = 145
assert N >= 5

timer = Timer()
visited = [[-1] * N for _ in range(N)]

dx = [-1, 1, 2,  2,  1, -1, -2, -2]
dy = [ 2, 2, 1, -1, -2, -2, -1,  1]

def get_degree(x, y):
    deg = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if not(0 <= nx <= N-1) or not(0 <= ny <= N-1):
            continue
        if visited[ny][nx] != -1:
            continue
        deg += 1
    return deg

def dfs(cnt, x, y):
    if not(0 <= x <= N-1) or not(0 <= y <= N-1):
        return False
    if visited[y][x] != -1:
        return False
    
    visited[y][x] = cnt
    if cnt == N*N:
        return True
    
    # heuristic
    s = {}
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        s[(nx, ny)] = get_degree(nx, ny)

    # choose the least degree
    ss = sorted(s.items(), key=lambda x: x[1])
    for nxy in ss:
        (nx, ny), _ = nxy
        if dfs(cnt+1, nx, ny):
            return True
    visited[y][x] = -1
    return False

if not dfs(1, N-1, N-1):
    print("[-] not found :(")

print("[*] Time:", timer.end())

if debug:
    for col in visited:
        print(col)

show_graph(visited, N)
