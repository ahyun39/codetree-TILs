def numb(n):
    if n % 2 == 0 or str(n)[-1] == '5' or (n % 3 == 0 and n % 9 != 0):
        return False
    return True
a, b = map(int,input().split())
ans = 0
for i in range(a, b+1):
    if numb(i):
        ans += 1
print(ans)