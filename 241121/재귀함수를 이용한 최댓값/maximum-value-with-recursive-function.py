def f(nums, i, now_max):
    if i == len(nums)-1:
        return now_max
    if nums[i] > now_max:
        return f(nums, i+1, nums[i])
    else:
        return f(nums, i+1, now_max)

def solution():
    n = int(input())
    nums = list(map(int, input().split()))
    print(f(nums, 0, -1))

solution()
