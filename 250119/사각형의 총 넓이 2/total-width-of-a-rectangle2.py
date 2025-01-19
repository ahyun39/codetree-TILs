N = int(input())
graph = [[0] * 201 for _ in range(201)]

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1+100, y2+100):
        for j in range(x1+100, x2+100):
            graph[i][j] = 1

ans = sum([sum(g) for g in graph])
print(ans)