n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
convenience_stores = [0]+[list(map(int,input().split())) for _ in range(m)]
check = [[0]*n for _ in range(n)]
people = [0] * (m+1)

def move(x,y,idx):
    cx, cy = convenience_stores[idx][0]-1, convenience_stores[idx][1]-1
    px, py = x, y
    dist = 1e9
    for dx, dy in [(-1,0),(0,-1),(0,1),(1,0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if dist > abs(cx - nx) + abs(cy - ny) and check[nx][ny] != -1:
                dist = abs(cx - nx) + abs(cy - ny)
                px, py = nx, ny
    return px, py

def basecamp(idx):
    cx, cy = convenience_stores[idx][0]-1, convenience_stores[idx][1]-1
    px, py = 0, 0
    dist = 1e9
    dist2 = 1e9
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1 and check[i][j] != -1:
                if dist >= abs(cx - i) + abs(cy - j):
                    for dx, dy in [(-1,0),(0,-1),(0,1),(1,0)]:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < n and 0 <= ny < n and check[nx][ny] != -1:
                            if dist2 > abs(cx - nx) + abs(cy - ny):
                                dist = abs(cx - i) + abs(cy - j)
                                dist2 = abs(cx - nx) + abs(cy - ny)
                                px, py = i, j
    return px, py

i = 1
while True:
    if i <= m:
        k = i
    else:
        k = m
    for j in range(1,k+1):
        if j >= i:
            px, py = basecamp(j)
            check[px][py] = -1
            people[j] = [px,py]
        else:
            if people[j] != 0:
                x, y = move(people[j][0], people[j][1], j)
                if x == convenience_stores[j][0]-1 and y == convenience_stores[j][1]-1:
                    check[x][y] = -1
                    people[j] = 0
                else:
                    people[j] = [x,y]
    if people.count(0) == m+1: break
    i += 1
print(i)