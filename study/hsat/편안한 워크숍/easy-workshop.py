N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

cells = []
for i in range(N):
    for j in range(N):
        cells.append((grid[i][j], i, j))

cells.sort()

def can(max_diff):
    dp = [[1]*N for _ in range(N)]

    for h, x, y in cells:
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if grid[nx][ny] < grid[x][y]:
                    if grid[x][y] - grid[nx][ny] <= max_diff:
                        dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)
        if dp[x][y] >= K:
            return True
    return False

left, right = 0, 10**9
answer = -1

while left <= right:
    mid = (left + right) // 2
    if can(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)