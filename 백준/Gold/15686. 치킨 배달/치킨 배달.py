import sys
from itertools import combinations
input = sys.stdin.readline

N,M = map(int,input().split())
house = []
chicken = []
city = [[0] * (N + 1)]
ans = []
for _ in range(N) :
    city.append([0] + list(map(int,input().split())))

for i in range(N + 1) :
    for j in range(N + 1) :
        if city[i][j] == 1 :
            house.append((i,j ))
        if city[i][j] == 2 :
            chicken.append((i,j))

for c in combinations(chicken,M) :
    t = 0
    for r1,c1 in house :
        min_nm = sys.maxsize
        for r2,c2 in c :
            min_nm = min(min_nm,abs(r1-r2) + abs(c1-c2))
        t += min_nm
    ans.append(t)
print(min(ans))