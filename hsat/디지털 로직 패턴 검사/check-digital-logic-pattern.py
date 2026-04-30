S = input().strip()
K, M = map(int, input().split())
N = len(S)

arr = [int(c) for c in S]


def check(L):
    hash_val = 0

    for i in range(L):
        hash_val = (hash_val << 1) | arr[i]

    count = {}

    count[hash_val] = 1
    if M == 1:
        return True

    mask = (1 << L) - 1

    for i in range(L, N):
        hash_val = ((hash_val << 1) & mask) | arr[i]

        cnt = count.get(hash_val, 0) + 1
        if cnt >= M:
            return True
        count[hash_val] = cnt

    return False

# 긴 패턴이 반복되면, 그 안의 짧은 패턴은 반드시 더 많이 반복된다.
print(1 if check(K) else 0)