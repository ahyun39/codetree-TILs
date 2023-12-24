k, n = map(int,input().split())
ans = []

def back():
    if len(ans) == n and (sum(ans)//(ans[0])) != 0: 
        print(" ".join(map(str, ans)))
        return 
    for i in range(1, k+1):
        if i not in ans:
            ans.append(i)
            back()
            ans.pop()
            
back()