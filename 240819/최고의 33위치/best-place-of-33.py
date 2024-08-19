n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

max_coins = 0
for i in range(n-2):
    for j in range(n-2):
        coins = sum(sum(graph[i+row][j:j+3]) for row in range(3))
        max_coins = max(max_coins, coins)

print(max_coins)