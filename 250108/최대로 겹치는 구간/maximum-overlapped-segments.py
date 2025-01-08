n = int(input())
lines = [0] * 201

for _ in range(n):
    a, b = map(int, input().split())
    a, b = a + 100, b + 100
    for i in range(a, b+1):
        lines[i] += 1

print(max(lines))