import sys

input = sys.stdin.readline

N = int(input())
stairs = [int(input()) for _ in range(N)]
DP = [0] * N

DP[0] = stairs[0]
if N > 1 :
  DP[1] = DP[0] + stairs[1]

if N > 2 :
  DP[2] = max(DP[0],stairs[1]) + stairs[2]
  
if N > 3 :
  for i in range(3,N) :
    DP[i] = max(DP[i - 3] + stairs[i - 1],DP[i - 2]) + stairs[i]
print(DP[-1])