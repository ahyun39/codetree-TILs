N = int(input())

def recur(idx):
    global answer
    answer += 1
    if idx >= N-1:
        return
    recur(idx+1)
    recur(idx+2)
    recur(idx+3)
    recur(idx+4)

answer = 0
recur(0)
print(answer)