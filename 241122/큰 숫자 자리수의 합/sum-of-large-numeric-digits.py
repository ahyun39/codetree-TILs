a, b, c = map(int, input().split())
num = str(a * b * c)

def f(num, i, s):
    if i == len(num):
        return s
    return f(num, i+1, s + int(num[i]))

print(f(num, 0, 0))