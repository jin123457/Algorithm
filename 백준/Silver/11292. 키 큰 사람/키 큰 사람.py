import sys

input = sys.stdin.readline

while True :
  N = int(input())
  if N == 0 : break

  obj = {}
  A = [list(input().split()) for _ in range(N)]
  for a in A :
    name,height = a
    height = height.split(".")[1]

    if height not in obj :
      obj[height] = []
      obj[height].append(name)
    else :
      obj[height].append(name)
  print(" ".join(sorted(obj.items(),reverse=True)[0][1]))