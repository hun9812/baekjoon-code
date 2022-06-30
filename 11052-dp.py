import sys
input = sys.stdin.readline

n = int(input())
p = [0] + list(map(int, input().split()))

dp_arr = [0, p[1]]

for i in range(2, n+1):
    cur_max = p[i]
    for j in range(1, i):
        cur_max = max(cur_max, dp_arr[j] + dp_arr[i-j])
    dp_arr.append(cur_max)

print(dp_arr[n])
