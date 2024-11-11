n = int(input())

def f(n, cnt):
    if n == 1:
        return cnt
    if n % 2 == 0:
        f(n//2, cnt + 1)
    elif n % 2 == 1:
        f(n%3, cnt + 1)
print(f(n, 0))