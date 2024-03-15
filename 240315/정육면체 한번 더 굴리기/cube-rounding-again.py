from collections import deque
n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
dice = [2,6,3] # 주사위의 앞면, 아랫면, 오른쪽면
now = "right" # 주사위가 현재 굴러가는 방향 
x, y = 0, 0 # 주사위의 위치
answer = 0

# 주사위가 보드 내 범위에 있는지 확인
def is_valid(x,y):
    return 0 <= x < n and 0 <= y < n

# 주사위가 구르면서 이동
def move(now, x, y):
    directions = {"left": (0, -1), "right": (0, 1), "up": (-1, 0), "down": (1, 0)}
    dx, dy = directions[now]
    nx, ny = x + dx, y + dy
    if not is_valid(nx, ny):
        nx, ny = nx - dx * 2, ny - dy * 2
        now = {"left": "right", "right": "left", "up": "down", "down": "up"}[now]
    return nx, ny, now

# 주사위가 놓여있는 칸에 적혀있는 숫자를 기준으로 상하좌우로 인접한 같은 숫자가 적혀있는 모든 칸의 합 구하기
# BFS algorithm
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

# 주사위가 굴러갈 때 주사위의 앞면, 아랫면, 오른쪽면의 값을 업데이트
def roll_dice(now, dice):
    front, floor, right = dice[0], dice[1], dice[2]
    if now in {"right", "left"}:
        dice = [front, right if now == "right" else 7-right, 7-floor if now == "right" else floor]
    else:
        dice = [floor if now == "up" else 7-floor, front if now == "down" else 7-front, right]
    return dice

# 주사위 아랫면 > 닿아있는 격자판에 적혀있는 숫자인 경우, 시계방향으로 전환
def clock_wise(now):
    clockwise_dict = {"right": "down", "left": "up", "down": "left", "up": "right"}
    return clockwise_dict[now]

# 주사위 아랫면 < 닿아있는 격자판에 적혀있는 숫자의 경우, 반시계방향으로 전환
def counter_clock_wise(now):
    counter_clock_wise_dict = {"right": "up", "left": "down", "down": "right", "up": "left"}
    return counter_clock_wise_dict[now]

if __name__ == "__main__":
    for _ in range(m):
        x, y, now = move(now, x, y)
        dice = roll_dice(now, dice)
        if dice[1] > board[x][y]: now = clock_wise(now)
        elif dice[1] < board[x][y]: now = counter_clock_wise(now)
        answer += score_(x,y)
    print(answer)