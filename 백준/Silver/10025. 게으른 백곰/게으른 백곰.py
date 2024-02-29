import sys

input = sys.stdin.readline

N,K = map(int,input().split())
P = {}
for _ in range(N) :
    G,X = map(int,input().split())
    P[X] = G

maxnm = max(P)
arr = [0] * (maxnm + 1)
ice = [0] * (maxnm + 1)
for i in P :
    arr[i] = P[i]
ice[0] = sum(arr[:K + 1])
for i in range(1,len(arr)) :

    ice[i] = ice[i - 1]

    if i > K :
        ice[i] -= arr[i - (K + 1)]
        if ice[i] < 0 : ice[i] = 0
    if i < len(arr) - K :
        ice[i] += arr[i + K]

print(max(ice))