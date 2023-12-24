# 변수 선언 및 입력:
n = int(input())
arr = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if arr[i] + arr[j] + arr[k] == (arr[i] | arr[j] | arr[k]):
                ans = max(ans, arr[i] + arr[j] + arr[k])

print(ans)