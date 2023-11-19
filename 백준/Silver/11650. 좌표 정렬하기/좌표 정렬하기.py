import sys

N = int(sys.stdin.readline())
obj = {}
for _ in range(N) :
  x,y = map(int,sys.stdin.readline().split())

  if x not in obj :
    obj[x] = [y]
  else :
    obj[x].append(y)

for nm in sorted(obj):
  obj[nm].sort()
  if len(obj[nm]) > 1 :
    for i in obj[nm] :
      print(f"{nm} {i}")
  else :
    print(f"{nm} {obj[nm][0]}")