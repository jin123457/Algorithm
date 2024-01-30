import sys

input = sys.stdin.readline

N = int(input())
if N == 0 :
    print(0)
else :
    arr = [0,1]

    for i in range(2,N + 1) :
        arr.append(arr[i - 1] + arr[i - 2])

    print(arr[-1])