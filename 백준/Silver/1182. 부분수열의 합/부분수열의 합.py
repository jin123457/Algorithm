import sys
from itertools import combinations
input = sys.stdin.readline

N,M = map(int,input().split())
nm = list(map(int,input().split()))
arr = []
ans = 0
for i in range(1,len(nm) + 1) :
    for c in combinations(nm,i) :
        arr.append(c)
for n in arr :
    if sum(list(n)) == M : ans += 1

print(ans)