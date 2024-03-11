import copy
n, m, k, c = map(int,input().split())
forest = [list(map(int,input().split())) for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(n):
        if forest[i][j] == -1:
            forest[i][j] = "-1"

def grow(x, y):
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    for d in directions:
        if 0 <= x + d[0] < n and 0 <= y + d[1] < n:
            if forest[x+d[0]][y+d[1]] != "-1" and forest[x+d[0]][y+d[1]] > 0:
                forest[x][y] += 1
    return forest

def breed(x, y, forest_breed):
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    near = 0
    for d in directions:
        if 0 <= x + d[0] < n and 0 <= y + d[1] < n:
            nx, ny = x + d[0], y + d[1]
            if forest[nx][ny] == 0:
                near += 1
    for d in directions:
        if 0 <= x + d[0] < n and 0 <= y + d[1] < n:
            nx, ny = x + d[0], y + d[1]
            if forest[nx][ny] == 0:
                forest_breed[nx][ny] += (forest[x][y] // near)
    return forest_breed

def remove(x,y,k,forest_remove):
    for i in range(1,k+1):
        if (0 <= x - i < n and 0 <= y - i < n):
            if forest[x-i][y-i] == "-1":
                break
            if forest[x-i][y-i] > 0:
                forest_remove[x][y] += forest[x-i][y-i]
    for i in range(1,k+1):
        if (0 <= x - i < n and 0 <= y + i < n):
            if forest[x-i][y+i] == "-1":
                break
            if forest[x-i][y+i] > 0:
                forest_remove[x][y] += forest[x-i][y+i]
    for i in range(1,k+1):
        if (0 <= x + i < n and 0 <= y - i < n):
            if forest[x+i][y-i] == "-1":
                break
            if forest[x+i][y-i] > 0:
                forest_remove[x][y] += forest[x+i][y-i]
    for i in range(1,k+1):
        if (0 <= x + i < n and 0 <= y + i < n):
            if forest[x+i][y+i] == "-1":
                break
            if forest[x+i][y+i] > 0:
                forest_remove[x][y] += forest[x+i][y+i]
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

    # 나무 제초제 위치 선청
    forest_remove = copy.deepcopy(forest)
    for i in range(n):
        for j in range(n):
            if forest[i][j] != "-1" and forest[i][j] > 0:
                forest_remove = remove(i,j,k,forest_remove)
    max_remove = 0
    rx, ry = 0, 0
    for i in range(n):
        for j in range(n):
            if forest_remove[i][j] != "-1" and forest_remove[i][j] > max_remove:
                max_remove = forest_remove[i][j]
                rx, ry = i, j
    answer += max_remove

    # 나무 제초제 뿌리기
    forest[rx][ry] = -c-1
    for i in range(1,k+1):
        if 0 <= rx - i < n and 0 <= ry - i < n:
            if forest[rx-i][ry-i] == "-1": break
            else: forest[rx-i][ry-i] = -c-1
    for i in range(1,k+1):
        if 0 <= rx - i < n and 0 <= ry + i < n:
            if forest[rx-i][ry+i] == "-1": break
            else: forest[rx-i][ry+i] = -c-1
    for i in range(1,k+1):
        if 0 <= rx + i < n and 0 <= ry - i < n:
            if forest[rx+i][ry-i] == "-1": break
            else: forest[rx+i][ry-i] = -c-1
    for i in range(1,k+1):
        if 0 <= rx + i < n and 0 <= ry + i < n:
            if forest[rx+i][ry+i] == "-1": break
            else: forest[rx+i][ry+i] = -c-1
    forest = remove_year(forest,n)

print(answer)