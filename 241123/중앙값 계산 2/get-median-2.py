n = int(input())
nums = list(map(int, input().split()))
nums.sort()

for i in range(n):
    if i % 2 == 0:
        print(nums[i//2], end=' ')