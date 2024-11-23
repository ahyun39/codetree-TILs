n = int(input())
nums = list(map(int, input().split()))

def f(n, nums, ans, i):
    if i == n:
        return ans
    if ans % nums[i] != 0:
        return f(n, nums, ans * nums[i], i+1)
    else:
        return f(n, nums, ans, i+1)

print(f(n, nums, 1, 0))