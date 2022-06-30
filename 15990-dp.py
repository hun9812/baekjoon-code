import sys
input = sys.stdin.readline


def plus123(max_num, input_arr):

    arr = [[0, 0, 0] for _ in range(max_num+1)]

    arr[1] = [1, 0, 0]
    arr[2] = [0, 1, 0]
    arr[3] = [1, 1, 1]

    for i in range(4, max_num+1):
        arr[i][0] = arr[i-1][1] % 1000000009 + arr[i-1][2] % 1000000009
        arr[i][1] = arr[i-2][0] % 1000000009 + arr[i-2][2] % 1000000009
        arr[i][2] = arr[i-3][0] % 1000000009 + arr[i-3][1] % 1000000009

    for i in input_arr:
        print(sum(arr[i]) % 1000000009)

    return


t = int(input())

input_arr = []

for i in range(t):
    input_arr.append(int(input()))

max_num = max(input_arr)

plus123(max_num, input_arr)
