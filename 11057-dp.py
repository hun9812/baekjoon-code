import sys
input = sys.stdin.readline

n = int(input())

dp_arr = [[0 for _ in range(10)] for _ in range(n+1)]
dp_arr[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp_arr[i][j] = 1
        else:
            dp_arr[i][j] = (dp_arr[i-1][j] + dp_arr[i][j-1]) % 10007

print(sum(dp_arr[n]) % 10007)
