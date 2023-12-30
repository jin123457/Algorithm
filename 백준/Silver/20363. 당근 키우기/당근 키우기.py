import sys

input = sys.stdin.readline

N,M = map(int,input().split())

if N > M :
   print(N + M + M // 10)
else :
   print(N + M + N // 10)