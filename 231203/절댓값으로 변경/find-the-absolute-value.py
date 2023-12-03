n = int(input())
numbers = list(map(int,input().split()))
for i in range(n): numbers[i] = abs(numbers[i])
print(*numbers)