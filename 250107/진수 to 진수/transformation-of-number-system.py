def trans(num, n):
    to_dec = 0
    nl = n[::-1]
    l = len(nl) - 1
    while True:
        if l < 0:
            break
        to_dec += (int(nl[l]) * (num ** l))
        l -= 1
    return to_dec

def trans_again(num2, to_dec):
    to_num2 = []
    while True:
        if to_dec < num2:
            to_num2.append(to_dec)
            break
        to_num2.append(to_dec % num2)
        to_dec //= num2
    return to_num2[::-1]

def f():
    a, b = map(int, input().split())
    n = str(input())
    to_dec = trans(a, n)
    ans = trans_again(b, to_dec)
    print(*ans, sep='')

f()