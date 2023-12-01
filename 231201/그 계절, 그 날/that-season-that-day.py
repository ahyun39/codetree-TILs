Y, M, D = map(int,input().split())

def leap(Y):
    if Y % 4 == 0:
        if Y % 100 == 0 and Y % 400 == 0:
            return True
        elif Y % 100 == 0:
            return False
        return True
    return False

def is_right(Y, M, D):
    if M in [1,3,5,7,8,10,12]:
        if 1 <= D <= 31:
            return True
    elif M in [4,6,9,11]:
        if 1 <= D <= 30:
            return True
    else:
        if leap(Y):
            if 1 <= D <= 29:
                return True
        else:
            if 1 <= D <= 28:
                return True

if is_right(Y, M, D):
    if M in [3,4,5]:
        print('Spring')
    elif M in [6,7,8]:
        print('Summer')
    elif M in [9,10,11]:
        print('Fall')
    else:
        print('Winter')
else:
    print(-1)