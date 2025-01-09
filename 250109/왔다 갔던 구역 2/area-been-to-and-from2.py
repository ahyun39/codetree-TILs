n = int(input())
now = 0
lines = {}

for _ in range(n):
    x, direct = map(str, input().split())
    x = int(x)
    
    if direct == 'L':
        for _ in range(x):
            lines[now] = lines.get(now,0) + 1
            now -= 1
    else:
        for _ in range(x):
            lines[now] = lines.get(now,0) + 1
            now += 1
    lines[now] = lines.get(now, 0) + 1

ans = 0
lines = sorted(lines.items())
point, v = lines[0][0], lines[0][1]

for key, value in lines[1:]:
    if value >= 2:
        if key == point + 1:
            ans += 1
        point = key

print(ans)


