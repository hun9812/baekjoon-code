import sys
input = sys.stdin.readline

n = int(input())

dp_arr = [sys.maxsize for _ in range(n+1)]
dp_arr[0] = 0

for i in range(1, n+1):
    cur_num = 1
    while (i - (cur_num**2)) >= 0:
        dp_arr[i] = min(dp_arr[i], dp_arr[i - (cur_num**2)] + 1)
        cur_num += 1

print(dp_arr[n])
