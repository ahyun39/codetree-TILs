n = int(input())

def f(n, cnt):
    if n == 1:
        return cnt
    if n % 2 == 0:
        return f(n//2, cnt + 1)
    else:
        return f(n * 3 + 1, cnt + 1)

print(f(n, 0))