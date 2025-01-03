n = int(input())

binary = []

while True:
    if n < 2:
        binary.append(n)
        break
    binary.append(n%2)
    n //= 2

print(*binary[::-1], sep='')