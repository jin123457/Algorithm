import sys

input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int,input().split()))
sum_arr = [0] * (N + 1)
for i in range(1,N + 1) :
    sum_arr[i] = arr[i] + sum_arr[i - 1]
    
M = int(input())
for _ in range(M) :
    i,j = map(int,input().split())
    print(sum_arr[j] - sum_arr[i - 1])
