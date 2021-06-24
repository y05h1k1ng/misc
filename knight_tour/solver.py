from utils import show_graph, Timer

debug = True
N = int(input("N = "))
assert N >= 5

timer = Timer()
visited = [[-1] * N for _ in range(N)]

dx = [-1, 1, 2,  2,  1, -1, -2, -2]
dy = [ 2, 2, 1, -1, -2, -2, -1,  1]

def dfs(cnt, x, y):
    if not(0 <= x <= N-1) or not(0 <= y <= N-1):
        return False
    if visited[y][x] != -1:
        return False
    
    visited[y][x] = cnt
    if cnt == N*N:
        return True
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
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
