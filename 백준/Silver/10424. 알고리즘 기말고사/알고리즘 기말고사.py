import sys

input = sys.stdin.readline

N = int(input())
M = list(map(int,input().split()))
F = [0] * N
for i,v in enumerate(M) :
    F[v - 1] = i + 1
for i in range(N) :
    print(i + 1 - F[i])