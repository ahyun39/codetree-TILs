n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    col_cnt = 1
    now_col = -1
    for j in range(n):
        if col_cnt >= m:
            break
        if graph[i][j] != now_col:
            col_cnt = 1
        elif graph[i][j] == now_col:
            col_cnt += 1
        now_col = graph[i][j]
    if col_cnt >= m:
        ans += 1

for i in range(n):
    row_cnt = 1
    now_row = -1
    for j in range(n):
        if row_cnt >= m:
            break
        if graph[j][i] != now_row:
            row_cnt = 1
        elif graph[j][i] == now_row:
            row_cnt += 1
        now_row = graph[j][i]
    if row_cnt >= m:
        ans += 1
print(ans)