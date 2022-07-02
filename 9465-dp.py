import sys
input = sys.stdin.readline

n = int(input())


def sticker(k, sticker_arr):
    for i in range(1, k):
        sticker_arr[0][i] = max(sticker_arr[0][i-1],
                                sticker_arr[1][i-1] + sticker_arr[0][i])
        sticker_arr[1][i] = max(sticker_arr[1][i-1],
                                sticker_arr[0][i-1] + sticker_arr[1][i])
    print(max(sticker_arr[0][k-1], sticker_arr[1][k-1]))
    return


for i in range(n):
    k = int(input())
    sticker_arr = [list(map(int, input().split())) for i in range(2)]
    sticker(k, sticker_arr)
