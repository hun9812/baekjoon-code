import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp_arr = [1 for i in range(n)]

for i in range(n-2, -1, -1):
    for j in range(i+1, n):
        if a[i] > a[j]:
            dp_arr[i] = max(dp_arr[i], dp_arr[j]+1)

print(max(dp_arr))
