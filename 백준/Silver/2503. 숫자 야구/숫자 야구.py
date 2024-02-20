import sys
from itertools import permutations
input = sys.stdin.readline


T = int(input())
data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
arr = list(permutations(data, 3))

for _ in range(T) :
  N,S,B = input().strip().split()
  cnt = 0
  for i in range(len(arr)) :
    strike = ball = 0
    i -= cnt
    for j in range(3) :
      if arr[i][j] == N[j] : strike += 1
      elif N[j] in arr[i] : ball += 1

    if strike != int(S) or ball != int(B) : 
      arr.remove(arr[i])
      cnt += 1

print(len(arr))