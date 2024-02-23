import sys

input = sys.stdin.readline

N,Q = map(int,input().split())
arr = sorted(map(int,input().split()))
sum_arr = [0] * (N + 1)
sum_arr[1] = arr[0]

for i in range(2,len(arr) + 1) :
    sum_arr[i] = sum_arr[i - 1] + arr[i - 1]

for _ in range(Q) :
    S,E = map(int,input().split())
    print(sum_arr[E] - sum_arr[S - 1])