import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

move_x = [-1, 0, 1, 0]
move_y = [0, 1, 0, -1]


def dfs(x, y, depth, value):
    global max_value
    if depth >= 4:
        if value > max_value:
            max_value = value
        return
    else:
        for i in range(4):
            cx = x+move_x[i]
            cy = y+move_y[i]
            if 0 <= cx < m and 0 <= cy < n:
                if not visited[cy][cx]:
                    visited[cy][cx] = 1
                    dfs(cx, cy, depth+1, value+arr[cy][cx])
                    visited[cy][cx] = 0


max_value = 0
visited = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 1, arr[i][j])
        visited[i][j] = 0


print(max_value)
