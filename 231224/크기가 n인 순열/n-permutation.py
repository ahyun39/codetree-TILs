from itertools import permutations

n = int(input())
num = [i for i in range(1,n+1)]

for i in permutations(num,n):
    print(*i)