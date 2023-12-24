k, n = map(int,input().split())
ans = []

def back():
    if len(ans) == n: 
        print(" ".join(map(str, ans)))
        return 

    for i in range(1, k+1): 
        if len(ans) >= 2 and i == ans[-1] and i == ans[-2]:
            continue
        else:
            ans.append(i)
            back()
            ans.pop()
        
            
back()