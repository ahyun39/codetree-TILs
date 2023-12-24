from itertools import permutations

n = int(input())
num = [i for i in range(1,n+1)]

p = list(permutations(num,n))

for i in p[::-1]:
    print(*i)