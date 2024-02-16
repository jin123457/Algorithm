import sys

input = sys.stdin.readline

T = 0
arr = [int(input()) for _ in range(10)]
arr.append(0)
TT = arr[0]
for i in range(len(arr) - 1) :
    N = arr[i]
    TN = arr[i + 1]
    T += N
    TT += TN
    if TT >= 100 : break
if abs(100 - T) < abs(100 - TT) :
    print(T)
else :
    print(TT)