k, n = map(int,input().split())

ans = []

def back():
    if len(ans) == n:
        print(" ".join(map(str, ans)))
        return 
    for i in range(1, k+1):
        ans.append(i)
        back()
        ans.pop()
            
back()