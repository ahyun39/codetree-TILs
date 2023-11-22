def lcm(n,m):
    ans = 0
    i = 1
    if n >= m:
        while True:
            if (n*i)%m == 0:
                ans = n*i
                break
            i += 1
    else:
        while True:
            if (m*i)%n == 0:
                ans = m*i
                break
            i += 1
    print(ans)
n, m = map(int,input().split())
lcm(n,m)