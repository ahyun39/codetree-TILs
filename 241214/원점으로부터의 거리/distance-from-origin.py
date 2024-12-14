def f(n):
    circles = []
    for i in range(n):
        a, b = map(int,input().split())
        circles.append((abs(0-a) + abs(0-b), i+1))
    circles.sort(key=lambda x: (x[0], x[1]))
    for circle in circles:
        print(circle[1])

n = int(input())
f(n)