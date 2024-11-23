n = int(input())
nums = list(map(int, input().split()))

for i in range(n):
    sort_nums = nums[:i+1]
    sort_nums.sort()
    if i % 2 == 0:
        print(sort_nums[i//2], end=' ')