from collections import deque
n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
dice = [2,6,3] # 앞, 바닥, 오른쪽 
now = "right"
x, y = 0, 0
answer = 0

def is_valid(x,y):
    return 0 <= x < n and 0 <= y < n

def move(now,x,y):
    if now == "left":
        nx, ny = x, y - 1
        if is_valid(nx,ny):
            x, y = nx, ny
        else:
            now = "right"
            x, y = nx, ny + 2
    elif now == "right":
        nx, ny = x, y + 1
        if is_valid(nx,ny):
            x, y = nx, ny
        else:
            now = "left"
            x, y = nx, ny - 2
    elif now == "up":
        nx, ny = x - 1, y
        if is_valid(nx,ny):
            x, y = nx, ny
        else:
            now = "down"
            x, y = nx + 2, ny
    elif now == "down":
        nx, ny = x + 1, y
        if is_valid(nx,ny):
            x, y = nx, ny
        else:
            now = "up"
            x, y = nx - 2, ny
    return x, y, now
def score_(x,y):
    now_score = board[x][y]
    cnt = 1
    visited = [[False]*n for _ in range(n)]
    q = deque()
    q.append((x,y))
    while q:
        nx, ny = q.popleft()
        visited[nx][ny] = True
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nnx, nny = nx + dx, ny + dy
            if is_valid(nnx,nny):
                if board[nnx][nny] == now_score and not visited[nnx][nny]:
                    q.append((nnx,nny))
                    visited[nnx][nny] = True
                    cnt += 1
    return cnt * now_score 

def roll_dice(now, dice):
    front, floor, right = dice[0], dice[1], dice[2]
    if now == "right":
        dice = [front, right, 7-floor]
    elif now == "left":
        dice = [front, 7-right, floor]
    elif now == "down":
        dice = [7-floor, front, right]
    elif now == "up":
        dice = [floor, 7-front , right]
    return dice

def clock_wise(now):
    if now == "right":
        now = "down"
    elif now == "left":
        now = "up"
    elif now == "down":
        now = "left"
    elif now == "up":
        now = "right"
    return now

def counter_clock_wise(now):
    if now == "right":
        now = "up"
    elif now == "left":
        now = "down"
    elif now == "down":
        now = "right"
    elif now == "up":
        now = "left"
    return now

for _ in range(m):
    x, y, now = move(now, x, y)
    dice = roll_dice(now, dice)
    if dice[1] > board[x][y]: now = clock_wise(now)
    elif dice[1] < board[x][y]: now = counter_clock_wise(now)
    answer += score_(x,y)

print(answer)