N = int(input())

def f(N):
    if N == 0:
        return
    print(N, end = ' ')
    f(N-1)

def g(i):
    if i == N+1:
        return 
    print(i, end = ' ')
    g(i+1)

g(1)
print()
f(N)