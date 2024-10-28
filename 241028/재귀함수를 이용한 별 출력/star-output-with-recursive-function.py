N = int(input())

def star(i):
    if i == N+1:
        return
    print("*" * i)
    star(i+1)

star(1)