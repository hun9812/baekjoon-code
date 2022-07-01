import sys
input = sys.stdin.readline

n = int(input())

input_arr = list(map(int, input().split()))

dp_arr = [0 for _ in range(n)]
dp_arr[0] = 1

for i in range(1, n):
    cur_max = 0
    for j in range(i):
        if input_arr[i] > input_arr[j]:
            cur_max = max(cur_max, dp_arr[j])
    dp_arr[i] = cur_max+1

print(max(dp_arr))
