n = int(input())
now = 0
lines = {}

for _ in range(n):
    x, direct = map(str, input().split())
    x = int(x)
    if direct == 'L':
        for _ in range(x):
            now -= 1
            lines[now] = lines.get(now,0) + 1
    else:
        for _ in range(x):
            now += 1
            lines[now] = lines.get(now,0) + 1

ans = sum([1 for point in lines.values() if point >= 2])
print(ans)