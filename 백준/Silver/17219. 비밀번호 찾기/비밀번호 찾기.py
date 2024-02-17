import sys

input = sys.stdin.readline

N,M = map(int,input().split())
obj = {}

for _ in range(N) : 
  site,ps = input().rstrip().split()

  if site not in obj :
    obj[site] = ps

for _ in range(M) :
  FS = input().rstrip()

  print(obj[FS])