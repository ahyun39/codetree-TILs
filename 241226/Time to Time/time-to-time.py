a, b, c, d = map(int, input().split())
minutes = 0

while True:
    if a == c and b == d:
        break
    b += 1
    minutes += 1

    if b == 60:
        a += 1
        b = 0

print(minutes)