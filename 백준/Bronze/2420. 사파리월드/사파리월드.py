import sys

input = sys.stdin.readline

N,M = map(int,input().split())
max_nm = max(N,M)
min_nm = min(N,M)

print(max_nm - min_nm)