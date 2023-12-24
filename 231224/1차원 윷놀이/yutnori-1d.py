n, m, k = map(int,input().split())
move = list(map(int,input().split()))
cnt = 0
i = 0
get = 0
answer = 0
while True:
    if i == n+1 or k == 0:
        break
    else:
        if get == len(move):
            get = 0
        else:
            if cnt + move[get] < m:
                cnt += move[get]
                get += 1
            elif cnt + move[get] == m:
                answer += 1
                cnt = 0
                get += 1
                k -= 1
            else:
                cnt = move[get]
                get += 1
                k -= 1
    i += 1
print(answer)