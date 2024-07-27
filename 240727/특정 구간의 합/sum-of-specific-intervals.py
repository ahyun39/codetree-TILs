n, m = map(int,input().split())
nums = list(map(int,input().split()))
for _ in range(m):
    a1, a2 = map(int,input().split())
    print(sum(nums[a1-1:a2]))