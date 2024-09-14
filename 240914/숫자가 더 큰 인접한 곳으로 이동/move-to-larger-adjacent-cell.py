from collections import deque

n, r, c = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
ans = [graph[r-1][c-1]]

visited = [[False]*n for _ in range(n)]
q = deque()
q.append((r-1, c-1))
now = ans[0]
while q:
    x, y = q.popleft()
    visited[x][y] = True
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and now < graph[nx][ny]:
            q.append((nx, ny))
            visited[nx][ny] = True
            ans.append(graph[nx][ny])
            now = graph[nx][ny]
            break
print(*ans)