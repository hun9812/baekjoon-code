import sys
input = sys.stdin.readline

n = int(input())

dp_arr = [[0, 0] for _ in range(n+1)]

dp_arr[1] = [0, 1]

for i in range(2, n+1):

    dp_arr[i][0] = sum(dp_arr[i-1])

    dp_arr[i][1] = dp_arr[i-1][0]

print(sum(dp_arr[n]))
