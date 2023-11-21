n = int(input())
for _ in range(n):
    k = []
    for i in range(n,0,-1):
        k.append(i)
    print(*k)