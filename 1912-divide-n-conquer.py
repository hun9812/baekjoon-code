#Divide and conquer

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))


def middle_sum(start, end, mid, arr):
    left_sum = arr[mid]
    left_cur = arr[mid]
    for i in range(mid-1, start, -1):
        left_cur += arr[i]
        left_sum = max(left_sum, left_cur)

    right_sum = arr[mid+1]
    right_cur = arr[mid+1]
    for i in range(mid+1, end+1):
        right_cur += arr[i]
        right_sum = max(right_sum, right_cur)

    return left_sum + right_sum


def continue_sum(start, end, arr):

    if start >= end:
        return arr[start]

    mid = (start+end)//2
    left_max = continue_sum(start, mid+1, arr)
    middle_max = middle_sum(start, end, mid, arr)
    right_max = continue_sum(mid+1, end, arr)

    if left_max >= right_max and left_max >= middle_max:
        return left_max
    elif right_max >= left_max and right_max >= middle_max:
        return right_max
    else:
        return middle_max


print(continue_sum(0, n-1, arr))
