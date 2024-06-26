MOD = 10007
n = int(input())

dp = [
    [
        [
            [0, 0]
            for _ in range(2)
        ]
        for _ in range(2)
    ]
    for _ in range(n + 2)
]
   
dp[1][0][0][0] = 1

for i in range(1, n + 1):
    # dp[i][0][0][0]에서 나올 수 있는 모양을 전부 갱신합니다.
    dp[i + 1][0][0][1] = (dp[i + 1][0][0][1] + dp[i][0][0][0]) % MOD
    dp[i + 1][1][0][0] = (dp[i + 1][1][0][0] + dp[i][0][0][0]) % MOD
    dp[i + 1][1][1][1] = (dp[i + 1][1][1][1] + dp[i][0][0][0]) % MOD

    # dp[i][0][0][1]에서 나올 수 있는 모양을 전부 갱신합니다.
    dp[i + 1][0][0][0] = (dp[i + 1][0][0][0] + dp[i][0][0][1]) % MOD
    dp[i + 1][1][1][0] = (dp[i + 1][1][1][0] + dp[i][0][0][1]) % MOD

    # dp[i][0][1][0]에서 나올 수 있는 모양을 전부 갱신합니다.
    dp[i + 1][1][0][1] = (dp[i + 1][1][0][1] + dp[i][0][1][0]) % MOD

    # dp[i][1][0][0]에서 나올 수 있는 모양을 전부 갱신합니다.
    dp[i + 1][0][0][0] = (dp[i + 1][0][0][0] + dp[i][1][0][0]) % MOD
    dp[i + 1][0][1][1] = (dp[i + 1][0][1][1] + dp[i][1][0][0]) % MOD

    # dp[i][0][1][1]에서 나올 수 있는 모양을 전부 갱신합니다.
    dp[i + 1][1][0][0] = (dp[i + 1][1][0][0] + dp[i][0][1][1]) % MOD

    # dp[i][1][0][1]에서 나올 수 있는 모양을 전부 갱신합니다.
    dp[i + 1][0][1][0] = (dp[i + 1][0][1][0] + dp[i][1][0][1]) % MOD

    # dp[i][1][1][0]에서 나올 수 있는 모양을 전부 갱신합니다.
    dp[i + 1][0][0][1] = (dp[i + 1][0][0][1] + dp[i][1][1][0]) % MOD

    # dp[i][1][1][1]에서 나올 수 있는 모양을 전부 갱신합니다.
    dp[i + 1][0][0][0] = (dp[i + 1][0][0][0] + dp[i][1][1][1]) % MOD

# n번째 열까지 전부 꽉 채웠고
# n + 1번째 열에는 튀어나온 모양이 없는 경우가 (=j값이 전부 0, 0, 0)
# 문제에서 원하는 완벽하게 채운 상태가 됩니다.
print(dp[n + 1][0][0][0])