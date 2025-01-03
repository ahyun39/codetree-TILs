n = int(input())

binary = []

while True:
    if n == 1:
        binary.append(1)
        break
    binary.append(n%2)
    n //= 2

print(*binary[::-1], sep='')