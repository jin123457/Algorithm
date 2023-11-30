from itertools import combinations

N = int(input())
arr = [i for i in range(N)]
print(len(list(combinations(arr,2))) * 2)