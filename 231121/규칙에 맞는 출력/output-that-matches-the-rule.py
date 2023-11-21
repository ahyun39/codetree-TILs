n = int(input())
for i in range(1,n+1):
    k = n
    t = []
    for j in range(i):
        t = [k] + t
        k -= 1
    print(*t)