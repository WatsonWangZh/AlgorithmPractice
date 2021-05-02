T = int(input())
for t in range(T):
    N, K, P = map(int, input().split())
    s = []
    for _ in range(N):
        s.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(1, K):
            s[i][j] += s[i][j-1]
        s[i].append(0)

    dp = [[0] * (P+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, P+1):
            for x in range(0, min(j, K)+1):
                dp[i][j] = max(dp[i][j], dp[i-1][j-x] + s[i-1][x-1])

    print('Case #%d: %d' % (t+1, dp[N][P]))