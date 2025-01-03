binary_n = str(input())[::-1]
l = len(binary_n) - 1
dec_n = 0

while True:
    if l < 0:
        break
    dec_n += (int(binary_n[l]) * (2 ** l))
    l -= 1

print(dec_n)