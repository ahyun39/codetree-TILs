from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
targets = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(m)]

visited = [[False] * n for _ in range(n)]

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ans = 0

def backtrack(x, y, idx):
    global ans

    if (x, y) == targets[idx]:
        idx += 1
        if idx == m:
            ans += 1
            return
    
    for dx, dy in direct:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and graph[nx][ny] == 0:
                visited[nx][ny] = True
                backtrack(nx, ny, idx)
                visited[nx][ny] = False
    

sx, sy = targets[0]
visited[sx][sy] = True
backtrack(sx, sy, 0)

print(ans)
