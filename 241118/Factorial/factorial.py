n = int(input())

def fac(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    return n * fac(n-1)

print(fac(n))