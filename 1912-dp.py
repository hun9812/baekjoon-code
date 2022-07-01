import sys
input = sys.stdin.readline

n = int(input())

input_arr = list(map(int, input().split()))

for i in range(1, n):
    if (input_arr[i-1] + input_arr[i]) > input_arr[i]:
        input_arr[i] = input_arr[i-1] + input_arr[i]

print(max(input_arr))
