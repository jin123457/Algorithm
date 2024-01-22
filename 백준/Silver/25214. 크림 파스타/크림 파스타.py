import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
dp = [0] * N
mn = A[0]
for i in range(len(A)) :
    if i == 0 : continue
    else :
      if A[i] > mn:
          dp[i] = max(dp[i],dp[i - 1],A[i] - mn)
      else :
          dp[i] = dp[i - 1]

    if mn > A[i] : mn = A[i]
print(*dp)