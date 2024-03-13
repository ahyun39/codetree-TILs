n, m, k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
participants = [[0]*n for _ in range(n)]
participant = []
answer = 0
for i in range(1,m+1):
    x, y = map(int,input().split())
    participants[x-1][y-1] = i
    participant.append([x-1,y-1])

exit_x, exit_y = map(int,input().split())
exit_x -= 1
exit_y -= 1
board[exit_x][exit_y] = "exit"

def is_valid(x,y):
    return 0 <= x < n and 0 <= y < n

def move(x,y):
    cnt = 0
    dist = abs(exit_x-x) + abs(exit_y-y)
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x + dx, y + dy
        if is_valid(nx,ny) and board[nx][ny] == "exit":
            cnt += 1
            return "exit", "exit", cnt
        elif is_valid(nx, ny) and board[nx][ny] == 0:
            if dist > abs(exit_x-nx) + abs(exit_y-ny):
                x, y = nx, ny
                cnt += 1
                break
    return x, y, cnt

def rec(x,y):
    dist = 1e9
    px, py = 0, 0
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        for i in range(1,n):
            nx, ny = x + i*dx, y + i*dy
            if not is_valid(nx,ny): break
            else:
                if sum(participants[nx]) != 0:
                    for j in range(n):
                        if participants[nx][j] != 0 and dist > abs(x-nx) + abs(y-j):
                            dist = abs(x-nx) + abs(y-j)
                            px, py = nx, j
    d = max(abs(exit_x - px), abs(exit_y - py))
    lx, ly = min(exit_x, px), min(exit_y, py)
    rx, ry = max(exit_x, px), max(exit_y, py)

    if rx - d >= 0: lx = rx - d
    if rx - d < 0: lx = 0
    if ry - d >= 0: ly = ry - d
    if ry - d < 0: ly = 0

    rx, ry = lx + d, ly + d

    return lx, ly, rx, ry

def rotate(lx, ly, rx, ry, exit_x, exit_y):
    board_rotate = []
    participants_rotate = []
    for i in range(lx, rx+1):
        board_rotate += board[i][ly:ry+1]
        participants_rotate += participants[i][ly:ry+1]
    i = 0
    for j in range(ry, ly-1, -1):
        for k in range(lx, rx+1):
            if board_rotate[i] == "exit":
                board[k][j] = "exit"
                exit_x, exit_y = k, j
            else:
                board[k][j] = max(board_rotate[i]-1,0)
            i += 1
    i = 0
    for j in range(ry, ly-1, -1):
        for k in range(lx, rx+1):
            participants[k][j] = participants_rotate[i]
            if participants_rotate[i] != 0:
                idx = participants_rotate[i]-1
                participant[idx] = [k,j]
            i += 1
    return board, participants, exit_x, exit_y

for i in range(k):
    exit_p = 0
    for j in range(len(participant)):
        if participant[j][0] != -1 and participant[j][1] != -1:
            x, y, cnt = move(participant[j][0],participant[j][1])
            answer += cnt
            if x == "exit" and y == "exit":
                participants[participant[j][0]][participant[j][1]] = 0
                participant[j] = [-1, -1]
                
            elif x != participant[j][0] or y != participant[j][1]:
                participants[x][y] = j+1
                participants[participant[j][0]][participant[j][1]] = 0
                participant[j] = [x, y]
        else:
            exit_p += 1
    if exit_p == m: break
    lx, ly, rx, ry = rec(exit_x,exit_y)
    board, participants, exit_x, exit_y = rotate(lx, ly, rx, ry, exit_x, exit_y)
                    
print(answer)
print(exit_x+1, exit_y+1)