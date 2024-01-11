import sys

input = sys.stdin.readline

dp = [0] * 101
dp[:6] = [0,1,1,1,2,2]
for i in range(5,101) :
    dp[i] = dp[i - 1] + dp[i - 5]
T = int(input())

for _ in range(T) :
    print(dp[int(input())])