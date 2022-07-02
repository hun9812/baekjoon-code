import sys
input = sys.stdin.readline

n = int(input())

dp_arr = [[0, 0, 0] for _ in range(n)]
dp_arr[0] = [1, 1, 1]

for i in range(1, n):
    dp_arr[i][0] = sum(dp_arr[i-1]) % 9901
    dp_arr[i][1] = dp_arr[i-1][0] % 9901 + dp_arr[i-1][2] % 9901
    dp_arr[i][2] = dp_arr[i-1][0] % 9901 + dp_arr[i-1][1] % 9901

print(sum(dp_arr[n-1]) % 9901)
