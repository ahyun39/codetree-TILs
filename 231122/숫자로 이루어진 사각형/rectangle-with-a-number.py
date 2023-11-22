n = int(input())
k = 1
for i in range(n):
    for j in range(n):
        if k == 10:
            k = 1
        if j == n-1:
            print(k)
        else:
            print(k, end = ' ')
        k += 1