import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
ans = 0


def find_max(arr):
    res = 0
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if arr[i][j-1] == arr[i][j]:
                cnt += 1
                res = max(res, cnt)
            else:
                cnt = 1

    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if arr[j-1][i] == arr[j][i]:
                cnt += 1
                res = max(res, cnt)
            else:
                cnt = 1
    return res


# change width
for i in range(n):
    for j in range(1, n):
        arr[i][j], arr[i][j-1] = arr[i][j-1], arr[i][j]
        ans = max(ans, find_max(arr))
        arr[i][j], arr[i][j-1] = arr[i][j-1], arr[i][j]

for i in range(n):
    for j in range(1, n):
        arr[j][i], arr[j-1][i] = arr[j-1][i], arr[j][i]
        ans = max(ans, find_max(arr))
        arr[j][i], arr[j-1][i] = arr[j-1][i], arr[j][i]

print(ans)
