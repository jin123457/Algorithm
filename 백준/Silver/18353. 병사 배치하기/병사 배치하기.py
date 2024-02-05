import sys

input = sys.stdin.readline

N = int(input())
SD = list(map(int,input().split()))
DP = [1] * N

for i in range(len(SD)) :
    for j in range(0,i) :
        if SD[i] < SD[j] :
            DP[i] = max(DP[i],DP[j] + 1)
print(N - max(DP))