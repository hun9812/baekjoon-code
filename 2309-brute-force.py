import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(9)]
arr_sum = sum(arr)
arr.sort()

for i in range(len(arr)-1):
    one_hundred = arr_sum - arr[i]
    for j in range(i+1, len(arr)):
        if one_hundred - arr[j] == 100:
            for k in range(len(arr)):
                if k != i and k != j:
                    print(arr[k])
            exit()
