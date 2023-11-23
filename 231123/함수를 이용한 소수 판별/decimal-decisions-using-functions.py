def odd(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

a, b = map(int,input().split())
odd_sum = 0
for i in range(a, b+1):
    if odd(i):
        odd_sum += i
print(odd_sum)