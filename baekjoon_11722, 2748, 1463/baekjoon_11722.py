if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)

    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        max_ = 0
        for j in range(i - 1, -1, -1):
            if a[i] < a[j] and max_ < dp[j]:
                max_ = dp[j]
        dp[i] = max_ + 1

    print(max(dp))

