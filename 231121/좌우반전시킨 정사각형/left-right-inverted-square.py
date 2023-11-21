n = int(input())
for i in range(n):
    k = []
    for j in range(n):
        k = [(i+1)*(j+1)] + k
    print(*k)