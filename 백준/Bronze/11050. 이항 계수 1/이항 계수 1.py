from itertools import combinations

N,M = map(int,input().split())
arr = [i for i in range(N)]
print(len(list(combinations(arr,M))))