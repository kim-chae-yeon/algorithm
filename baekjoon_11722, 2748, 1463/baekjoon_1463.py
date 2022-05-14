if __name__ == "__main__":
    n = int(input())
    dp = [10000] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        if i == 2 or i == 3:
            dp[i] = 1
        else:
            if dp[i] > dp[i - 1] + 1:
                dp[i] = dp[i - 1] + 1
            if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
                dp[i] = dp[i // 3] + 1
            if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
                dp[i] = dp[i // 2] + 1

    print(dp[n])

