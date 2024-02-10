import sys
from itertools import combinations

input = sys.stdin.readline

T = int(input())
arr = [list(map(int,input().split())) for _ in range(T)]

if T == 1 :
    max_nm = max(arr[0])
    min_nm = min(arr[0])
    print(max_nm - min_nm)
else :
    ans = sys.maxsize
    for i in range(1,len(arr) + 1) :
        for c in combinations(arr,i) :
            sour = 1
            bitter = 0
            for k in c :
                sour *= k[0]
                bitter += k[1]
            max_nm = max(sour,bitter)
            min_nm = min(sour,bitter)
            if ans > max_nm - min_nm :
                ans = max_nm - min_nm
    print(ans)