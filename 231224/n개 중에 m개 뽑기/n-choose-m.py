from itertools import combinations

n, m = map(int,input().split())
num = [i for i in range(1,n+1)]
for i in combinations(num,m):
    print(*i)