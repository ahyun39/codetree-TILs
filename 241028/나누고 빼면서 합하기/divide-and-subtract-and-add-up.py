n, m = map(int, input().split())
A = list(map(int, input().split()))

def f(m):
    ans = A[m-1]
    while m != 1:
        if m % 2 == 0:
            m //= 2
        else:
            m -= 1
        ans += A[m-1]
    print(ans)

f(m)