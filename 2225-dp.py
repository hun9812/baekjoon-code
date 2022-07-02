import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp_arr = [[1 for _ in range(n+1)] for _ in range(k+1)]

for i in range(k+1):
    dp_arr[i][0] = 0
    dp_arr[i][1] = i

for i in range(2, k+1):
    for j in range(2, n+1):
        dp_arr[i][j] = dp_arr[i][j-1] + dp_arr[i-1][j]

print(dp_arr[k][n] % 1000000000)
