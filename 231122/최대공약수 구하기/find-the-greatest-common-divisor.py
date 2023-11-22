def gcd(n,m):
    ans = 0
    if n >= m:
        for i in range(m,0,-1):
            if m%i==0 and n%i==0:
                ans = i
                break
    else:
        for i in range(n,0,-1):
            if m%i==0 and n%i==0:
                ans = i
                break
    print(ans)
n, m = map(int,input().split())
gcd(n,m)