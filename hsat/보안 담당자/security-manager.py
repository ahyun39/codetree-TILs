N = int(input())
records = input()

# 길이 홀수면 무조건 불가능
if N % 2 != 0:
    print("No")
    exit()

low = 0   # 최소 열린 괄호: “최대한 많이 닫았을 때 남는 열린 괄호”
high = 0  # 최대 열린 괄호: “최대한 많이 열었을 때 남는 열린 괄호”

for ch in records:
    if ch == "(":
        low += 1
        high += 1
    elif ch == ")":
        low -= 1
        high -= 1
    else:  # '?'
        low -= 1 # 닫는 경우 -> 최소 열린 기호가 하나 줄어든다.
        high += 1 # 여는 경우 -> 최대 열린 기호가 하나 증가한다.

    low = max(low, 0)

    # 최대도 음수면 불가능
    if high < 0:
        print("No")
        exit()

print("Yes" if low == 0 else "No")