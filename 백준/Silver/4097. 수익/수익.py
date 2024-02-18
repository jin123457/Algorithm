import sys

input = sys.stdin.readline

while True :
    T = int(input())
    if T == 0 : break
    arr = [int(input()) for _ in range(T)]
    dp = [0] * T
    dp[0] = arr[0]
    for i in range(1,len(arr)) :
        dp[i] = max(dp[i-1] + arr[i], arr[i])
    print(max(dp))