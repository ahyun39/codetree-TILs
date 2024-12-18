n = int(input())
nums = list(map(int, input().split()))

nums_idx = [(i+1, j) for i, j in enumerate(nums)]
sort_nums = sorted(nums_idx, key=lambda x:x[1])

idx = []
for num_tuple in nums_idx:
    idx.append(sort_nums.index(num_tuple)+1)

print(*idx)