def is_leap(n):
    if n % 4 == 0:
        if n % 100 == 0 and n % 400 == 0:
            return 'true'
        elif n % 100 == 0:
            return 'false'
        return 'true'
    return 'false'

y = int(input())
print(is_leap(y))