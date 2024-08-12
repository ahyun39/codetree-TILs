n = int(input())
homes = list(map(int,input().split()))
min_dist = float('inf')
for i in range(n):
    dist = 0
    for j in range(n):
        dist += homes[j] * abs(j-i)
    if min_dist > dist:
        min_dist = dist
print(min_dist)