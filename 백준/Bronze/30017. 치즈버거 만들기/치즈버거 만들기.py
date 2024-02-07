import sys

input = sys.stdin.readline

N,M = map(int,input().split())

if N < M or N - M < 2 :
    print(N + (N - 1))
else :
    print(M + M + 1)