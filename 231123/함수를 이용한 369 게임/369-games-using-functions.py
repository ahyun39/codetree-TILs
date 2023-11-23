def t_s_n(n):
    return '3' in str(n) or '6' in str(n) or '9' in str(n) or n%3 == 0

a, b = map(int,input().split())
cnt = 0
for i in range(a, b+1):
    if t_s_n(i):
        cnt += 1
print(cnt)