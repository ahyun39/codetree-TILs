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

def score(x,y):
    now_score = board[x][y]
    cnt = 1
    check = 0
    # 위로 탐색 
    for i in range(1,n):
        nx = x - i
        if nx < 0: break
        else:
            if board[nx][y] != now_score: break
            for j in range(n):
                ny = y - j
                if ny < 0: break
                else:
                    if board[nx][ny] == now_score: cnt += 1
                    else:
                        check = 1
                        break
            for j in range(1,n):
                ny = y + j
                if ny >= n: break 
                else:
                    if board[nx][ny] == now_score: cnt += 1
                    else:
                        break
    # 동일 행 탐색
    for j in range(1,n):
        ny = y - j
        if ny < 0: break
        else:
            if board[x][ny] == now_score: cnt += 1
            else:
                break
    for j in range(1,n):
        ny = y + j
        if ny >= n: break 
        else:
            if board[x][ny] == now_score: cnt += 1
            else:
                break
    # 아래로 탐색
    for i in range(1,n):
        nx = x + i
        if nx >= n: break
        else:
            if board[nx][y] != now_score: break
            for j in range(n):
                ny = y - j
                if ny < 0: break
                else:
                    if board[nx][ny] == now_score: cnt += 1
                    else:
                        break
            for j in range(1,n):
                ny = y + j
                if ny >= n: break 
                else:
                    if board[nx][ny] == now_score: cnt += 1
                    else:
                        break
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
    answer += score(x,y)

print(answer)