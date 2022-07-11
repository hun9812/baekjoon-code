import sys
input = sys.stdin.readline

t = int(input())


def kaying(m, n, x, y):
    while not(x == y):
        if x > m*n*2:
            return -1
        elif x < y:
            x += m
        else:
            y += n
    return x


for i in range(t):
    m, n, x, y = map(int, input().split())
    print(kaying(m, n, x, y))
