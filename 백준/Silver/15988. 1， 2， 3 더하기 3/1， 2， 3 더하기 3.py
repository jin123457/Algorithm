import sys

input = sys.stdin.readline

arr = [0,1,2,4]
for _ in range(1000000) :
    arr.append((arr[-1] + arr[-2] + arr[-3]) % 1000000009)
T = int(input())
for _ in range(T) :
    N = int(input())
    print(arr[N])