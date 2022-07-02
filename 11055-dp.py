import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp_arr = [i for i in a]


for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            dp_arr[i] = max(dp_arr[i], dp_arr[j] + a[i])

print(max(dp_arr))
