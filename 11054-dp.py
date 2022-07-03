import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp_arr = [[1 for _ in range(n)] for _ in range(2)]

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            dp_arr[0][i] = max(dp_arr[0][i], dp_arr[0][j] + 1)

for i in range(n-2, -1, -1):
    for j in range(n-1, i, -1):
        if a[i] > a[j]:
            dp_arr[1][i] = max(dp_arr[1][i], dp_arr[1][j] + 1)

res = 0
for i in range(n):
    res = max(res, dp_arr[0][i] + dp_arr[1][i] - 1)

print(res)
