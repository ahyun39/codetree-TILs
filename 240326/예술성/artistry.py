from collections import deque

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
answer = 0

def is_valid(x,y):
    return 0 <= x < n and 0 <= y < n

# 그룹 표시
def make_group(board, group_board):
    def bfs(x,y,group,cnt):
        q = deque()
        q.append((x,y))
        while q:
            x, y = q.popleft()
            group_board[x][y] = group
            cnt += 1
            for dx, dy in [(-1,0),(0,1),(1,0),(0,-1)]:
                nx, ny = x + dx, y + dy
                if is_valid(nx,ny) and board[nx][ny] == now and group_board[nx][ny] == 0 and (nx,ny) not in q:
                    q.append((nx,ny))
        return cnt

    now = board[0][0]
    group = 1
    now_group = group
    for i in range(n):
        for j in range(n):
            if group_board[i][j] == 0:
                if now != board[i][j] or board[i][j] != now_group:
                    now = board[i][j]
                    group += 1
                groups[group] = [bfs(i,j,group,0),now]

def score(board, groups, scores):
    groups_idx = list(groups.keys())
    for i in range(len(groups_idx)-1):
        for j in range(i+1,len(groups_idx)):
            g1, g2 = groups_idx[i], groups_idx[j]
            lines = 0 # 맞닿아 있는 변의 수
            for a in range(n):
                for b in range(n):
                    if group_board[a][b] == g1:
                        for dx, dy in [(-1,0),(0,1),(1,0),(0,-1)]:
                            nx, ny = a + dx, b + dy
                            if is_valid(nx,ny) and group_board[nx][ny] == g2:
                                lines += 1
            if lines > 0:
                scores += (groups[g1][0] + groups[g2][0]) * groups[g1][1] * groups[g2][1] * lines 
    return scores 


def rotate(board):
    # 십자가 회전
    row = board[n//2]
    col = [board[i][n//2] for i in range(n)]
    board[n//2] = col
    for i in range(n):
        board[i][n//2] = row[-i-1]
    # 정사각형 회전
    b = []
    for i in range(n//2):
        b += board[i][:n//2]
    b = deque(b)
    while b:
        for i in range(n//2-1,-1,-1):
            for j in range(n//2):
                board[j][i] = b.popleft()
    b = []
    for i in range(n//2):
        b += board[i][n//2+1:]
    b = deque(b)
    while b:
        for i in range(n-1,n//2,-1):
            for j in range(n//2):
                board[j][i] = b.popleft()
    b = []
    for i in range(n//2+1,n):
        b += board[i][:n//2]
    b = deque(b)
    while b:
        for i in range(n//2-1,-1,-1):
            for j in range(n//2+1,n):
                board[j][i] = b.popleft()
    b = []
    for i in range(n//2+1,n):
        b += board[i][n//2+1:]
    b = deque(b)
    while b:
        for i in range(n-1,n//2,-1):
            for j in range(n//2+1,n):
                board[j][i] = b.popleft()
    return board

for _ in range(4):
    group_board = [[0]*n for _ in range(n)]
    groups = {}
    make_group(board,group_board)
    scores = score(board,groups,0)
    answer += scores
    board = rotate(board)
print(answer)