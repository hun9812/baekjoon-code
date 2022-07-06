import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
if m:
    broken_button = set(input().split())
else:
    broken_button = set()


res = abs(n-100)

for i in range(1000000):
    for j in str(i):
        if j in broken_button:
            break
    else:
        res = min(res, len(str(i)) + abs(n-i))


print(res)
