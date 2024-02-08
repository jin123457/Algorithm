import sys
input = sys.stdin.readline

N = int(input())

DP = [0] * N

DP[0] = 1
if N > 1 :
  DP[1] = 2

for i in range(2,N) :
  DP[i] = (DP[i - 1] + DP[i - 2]) % 10

print(DP[-1])