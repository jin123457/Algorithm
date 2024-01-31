import sys

input = sys.stdin.readline

N = int(input())
D = list()
V = list()
DP = [0 for _ in range(N + 1)]

for _ in range(N) :
    d,v = map(int,input().split())
    D.append(d)
    V.append(v)

for i in range(N - 1,-1,-1) :
    if i + D[i] > N : DP[i] = DP[i + 1]
    else : DP[i] = max(DP[i + 1],DP[D[i] + i] + V[i])
print(DP[0])