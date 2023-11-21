n = int(input())
for i in range(n):
    if i == 0 or i == n-1:
        print('* ' * n)
    else:
        print('* ' * i, end = '')
        print('  ' * (n-i-1), end = '')
        print('* ')