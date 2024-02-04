import sys

input = sys.stdin.readline

while True :
  N,M = map(int,input().split())
  if N == M == 0 : break
  obj = {}
  for _ in range(N) :
    for num in input().split() :
      if num not in obj :
        obj[num] = 1
      else :
        obj[num] += 1
  max_nm = sorted(obj.values(),reverse=True)[1]
  ans = []
  for nm in obj :
    if obj[nm] == max_nm :
      ans.append(int(nm))
  
  print(*sorted(ans))