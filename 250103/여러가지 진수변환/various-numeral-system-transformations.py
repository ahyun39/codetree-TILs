N, B = map(int, input().split())
arr = []

while True:
    if N < B:
        arr.append(N)
        break
    arr.append(N % B)
    N //= B

print(*arr[::-1], sep='')