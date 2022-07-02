import sys
input = sys.stdin.readline

n = int(input())

phodo = [0] + [int(input()) for _ in range(n)]

dp = [0 for _ in range(n+1)]

dp[1] = phodo[1]
if n > 1:
    dp[2] = phodo[2]+phodo[1]

for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-3]+phodo[i-1]+phodo[i], dp[i-2]+phodo[i])

print(dp[n])
