M, D = map(int,input().split())
def solution(M, D):
    if 1 <= M <= 12:
        if M in [1,3,5,7,8,10,12]:
            if 1 <= D <= 31:
                print("Yes")
            else:
                print("No")
        elif M in [4,6,9,11]:
            if 1 <= D <= 30:
                print("Yes")
            else:
                print("No")
        else:
            if 1 <= D <= 28:
                print("Yes")
            else:
                print("No")
    else:
        print("No")
solution(M,D)