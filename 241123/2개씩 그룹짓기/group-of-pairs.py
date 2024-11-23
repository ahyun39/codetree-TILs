n = int(input())
nums = list(map(int, input().split()))
nums.sort()
ans = -1
for i in range(0, n):
    if ans < nums[i] + nums[-1-i]:
        ans = nums[i] + nums[-1-i]
print(ans)