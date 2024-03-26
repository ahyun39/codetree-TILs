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

    now = board[0][0] # 현재 탐색 중인 숫자
    group = str(1) # 그룹 
    now_group = group # 그룹이 다른데 숫자가 같은 경우 같은 그룹으로 묶이는 것을 방지하기 위한 변수
    for i in range(n):
        for j in range(n):
            if group_board[i][j] == 0:
                if now != board[i][j] or board[i][j] != now_group:
                    now = board[i][j]
                    group = str(int(group) + 1)
                    now_group = group
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
            if lines > 0: # 맞닿아 있는 변이 하나라도 있는 경우 점수를 구한다.
                scores += (groups[g1][0] + groups[g2][0]) * groups[g1][1] * groups[g2][1] * lines 
    return scores 


def rotate_cross(board): # 십자 모양 반시계 방향으로 90도 회전
    row = board[n//2]
    col = [board[i][n//2] for i in range(n)]
    board[n//2] = col
    for i in range(n):
        board[i][n//2] = row[-1-i]

def rotate_square(board): # 십자 모양을 제외한 4개의 정사각형을 각각 시계 방향으로 90도 회전
    def rotate_square_section(board,start_row, end_row, start_col, end_col,b):
        b = deque(b)
        while b:
            for i in range(end_row-1,start_row-1, -1):
                for j in range(start_col,end_col):
                    board[j][i] = b.popleft()
    # 좌측 상단
    b = []
    for i in range(n//2):
        b += board[i][:n//2]
    rotate_square_section(board, 0, n//2, 0, n//2, b)
    # 우측 상단 
    b = []
    for i in range(n//2):
        b += board[i][n//2+1:]
    rotate_square_section(board, n//2+1, n, 0, n//2, b)
    # 좌측 하단
    b = []
    for i in range(n//2+1, n):
        b += board[i][:n//2]
    rotate_square_section(board, 0, n//2, n//2+1, n, b)
    # 우측 하단
    b = []
    for i in range(n//2+1, n):
        b += board[i][n//2+1:]
    rotate_square_section(board, n//2+1, n, n//2+1, n, b)

def rotate(board):
    rotate_cross(board)
    rotate_square(board)
    return board

for _ in range(4):
    group_board = [[0]*n for _ in range(n)]
    groups = {}
    make_group(board,group_board) # 그룹으로 나눈 후
    scores = score(board,groups,0) # 예술 점수를 구한다.
    answer += scores
    board = rotate(board) #회전
print(answer)