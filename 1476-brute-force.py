import sys
input = sys.stdin.readline

e, s, m = map(int, input().split())

while not(e == s and s == m):
    if e <= s and e <= m:
        e += 15
    elif s <= e and s <= m:
        s += 28
    else:
        m += 19

print(e)
