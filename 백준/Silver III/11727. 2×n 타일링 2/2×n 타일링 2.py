import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
DP = [0] * N
DP[0] = 1
if N > 1 :
    DP[1] = 3 

for i in range(2,N) :
    DP[i] = (DP[i - 2] * 2 + DP[i - 1]) % 10007

print(DP[-1])