a, o, c = map(str,input().split())
if o not in ['+', '-', '/', '*']:
    print(False)
else:
    ans = 0
    a = int(a)
    c = int(c)

    if o == '+':
        ans = a + c
    elif o == '-':
        ans = a - c
    elif o == '/':
        ans = a // c
    else:
        ans = a * c
    print(a, o, c, '=', ans)