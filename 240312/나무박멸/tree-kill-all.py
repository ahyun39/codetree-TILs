import copy
n, m, k, c = map(int,input().split())
forest = [list(map(int,input().split())) for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(n):
        if forest[i][j] == -1:
            forest[i][j] = "-1"

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < n

def grow(x, y):
    near = sum(1 for dx, dy in directions if is_valid(x + dx, y + dy) and forest[x+dx][y+dy] != "-1" and forest[x + dx][y + dy] > 0)
    forest[x][y] += near
    return forest

def breed(x, y, forest_breed):
    near = sum(1 for dx, dy in directions if is_valid(x + dx, y + dy) and forest[x+dx][y+dy] != "-1" and forest[x + dx][y + dy] == 0)
    if near > 0:
        breeds = forest[x][y] // near
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and forest[nx][ny] == 0:
                forest_breed[nx][ny] += breeds
    return forest_breed

def remove(x,y,k,forest_remove):
    for dx, dy in [(1,1),(1,-1),(-1,1),(-1,-1)]:
        for i in range(1, k+1):
            nx, ny = x + i * dx, y + i *dy
            if not is_valid(nx,ny) or forest[nx][ny] == "-1" or forest[nx][ny] <= 0:
                break
            elif forest[nx][ny] > 0: forest_remove[x][y] += forest[nx][ny]
    return forest_remove

# 나무 제초제 유지 기간
def remove_year(forest, n):
    for i in range(n):
        for j in range(n):
            if forest[i][j] != "-1" and forest[i][j] < 0:
                forest[i][j] += 1
    return forest

for _ in range(m):
    
    # 나무 성장
    for i in range(n):
        for j in range(n):
            if forest[i][j] != "-1" and forest[i][j] > 0:
                forest = grow(i,j)
    
    # 나무 번식
    forest_breed = copy.deepcopy(forest)
    for i in range(n):
        for j in range(n):
            if forest[i][j] != "-1" and forest[i][j] > 0:
                forest_breed = breed(i,j,forest_breed)
    forest = forest_breed
    
    # 나무 제초제 위치 선정
    forest_remove = copy.deepcopy(forest)
    for i in range(n):
        for j in range(n):
            if forest[i][j] != "-1" and forest[i][j] > 0:
                forest_remove = remove(i,j,k,forest_remove)
    max_remove = 0
    rx, ry = 0,0
    for i in range(n):
        for j in range(n):
            if forest_remove[i][j] != "-1" and forest_remove[i][j] > max_remove:
                max_remove = forest_remove[i][j]
                rx, ry = i, j
    answer += max_remove
    
    # 나무 제초제 뿌리기
    forest[rx][ry] = -c-1
    for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        for i in range(1, k + 1):
            nx, ny = rx + i * dx, ry + i * dy
            if not is_valid(nx, ny) or forest[nx][ny] == "-1":
                break
            elif forest[nx][ny] <= 0:
                forest[nx][ny] = -c-1
                break
            else: forest[nx][ny] = -c-1

    forest = remove_year(forest, n)
print(answer)