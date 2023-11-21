n = int(input())
for i in range(n):
    for j in range(n-i):
        if j == n-i-1:
            print(f'{i+1} * {j+1} = {(i+1)*(j+1)}')
        else:
            print(f'{i+1} * {j+1} = {(i+1)*(j+1)}', end = ' / ')