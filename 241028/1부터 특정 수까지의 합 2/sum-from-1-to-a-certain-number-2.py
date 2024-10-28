N = int(input())
ans = 0
def f(i):
    global ans

    if i == N+1:
        return
    ans += i
    f(i+1)
f(1)
print(ans)