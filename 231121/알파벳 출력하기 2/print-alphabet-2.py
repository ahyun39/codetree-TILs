from string import ascii_uppercase

n = int(input())
alpha_list = list(ascii_uppercase)

k = 0
for i in range(n):
    t = [' ' for _ in range(i)]
    for j in range(n-i):
        if k == 26:
            k = 0
        t.append(alpha_list[k])
        k += 1
    print(*t)