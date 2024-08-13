from itertools import combinations

n = int(input())
nums = list(map(int,input().split()))
nums.sort()
min_maxsum = 0
for i in range(n):
    if min_maxsum < nums[i] + nums[(2 * n)-i-1]:
        min_maxsum = nums[i] + nums[(2 * n)-i-1]
print(min_maxsum)