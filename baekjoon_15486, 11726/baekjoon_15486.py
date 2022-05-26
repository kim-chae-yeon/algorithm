import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    a.insert(0, 0)

    dp = [0] * (n + 2)

    max_ = 0
    for i in range(1, n + 1):
        if max_ < dp[i]:
            max_ = dp[i]

        if i + a[i][0] > n + 1:
            continue

        else:
            dp[i + a[i][0]] = max(max_ + a[i][1], dp[i + a[i][0]])

    if max_ < dp[n + 1]:
        max_ = dp[n + 1]
    print(max_)

