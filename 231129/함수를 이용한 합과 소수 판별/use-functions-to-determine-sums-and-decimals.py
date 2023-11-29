a, b = map(int,input().split())
ans = 0

def dec(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def sum_even(n):
    n = str(n)
    s = 0
    for i in range(len(n)):
        s += int(n[i])
    if s % 2 == 0:
        return True
    else:
        return False

for k in range(a, b+1):
    if dec(k):
        if sum_even(k):
            ans += 1
print(ans)