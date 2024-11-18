n = int(input())

def recursive_sum(n, current=1, ans=0):
    if current > n:
        return ans
    if (n % 2 == 0 and current % 2 == 0) or (n % 2 == 1 and current % 2 == 1):
        ans += current
    return recursive_sum(n, current + 1, ans)

print(recursive_sum(n))