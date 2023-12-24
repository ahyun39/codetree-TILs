k, n = map(int,input().split())

ans = []

def back():
    if len(ans) == n: # 배열의 길이를 확인
        print(" ".join(map(str, ans)))
        return 
    for i in range(1, k+1): # 1 ~ N 까지
        ans.append(i) # 배열 추가
        back() # 재귀
        ans.pop()
            
back()