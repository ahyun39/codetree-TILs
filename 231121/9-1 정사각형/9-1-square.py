n = int(input())
t = 9
for i in range(n):
    for j in range(n):
        if t == 0:
            t = 9
        if j == n-1:
            print(t)
            t -= 1
        else:
            print(t,end='')
            t -= 1