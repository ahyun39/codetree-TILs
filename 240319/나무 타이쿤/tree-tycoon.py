def is_valid(x,y):
    return 0 <= x < n and 0 <= y < n

def move(x,y,order,time):
    nutrients[x][y] = 0
    nx, ny = (x + time * directions[order][0]) % n, (y + time * directions[order][1]) % n
    move_nutrients[nx][ny] = 1
    board[nx][ny] += 1

def grow(x,y):
    cnt = 0
    for dx, dy in [(-1,-1),(1,-1),(-1,1),(1,1)]:
        nx, ny = x + dx, y + dy
        if is_valid(nx,ny) and board[nx][ny] > 0:
            cnt += 1
    return cnt

if __name__ == '__main__':

    n, m = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    nutrients = [[0]*n for _ in range(n)]
    nutrients[-1][0:2], nutrients[-2][0:2] = [1,1], [1,1] # 초기의 특수 영양제
    move_nutrients = [[0]*n for _ in range(n)]
    answer = 0
    directions = [(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1)]

    for _ in range(m):
        order, time = map(int,input().split())
        for i in range(n):
            for j in range(n):
                if nutrients[i][j] == 1:
                    move(i,j,order-1,time)
        for i in range(n):
            for j in range(n):
                if move_nutrients[i][j] == 1:
                    board[i][j] += grow(i,j)
        for i in range(n):
            for j in range(n):
                if board[i][j] >= 2 and move_nutrients[i][j] == 0:
                    board[i][j] -= 2
                    nutrients[i][j] = 1
                elif move_nutrients[i][j] == 1:
                    move_nutrients[i][j] = 0
    for b in board:
        answer += sum(b)
    print(answer)