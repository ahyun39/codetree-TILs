n = int(input())
t = 1
for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            if j == n-1:
                print(t)
                t += 2
            else:
                print(t, end = ' ')
                t += 1
        elif i % 2 != 0:
            if j == n-1:
                print(t)
                t += 1
            else:
                print(t, end = ' ')
                t += 2