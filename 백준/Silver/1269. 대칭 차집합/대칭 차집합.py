import sys
N,M = map(int,sys.stdin.readline().split()) # 도감의 있는 포켓몬 개수는 N, 맞춰야하는 포켓문 문제의 개수는 M
A_arr = list(map(int,sys.stdin.readline().split()))
B_arr = list(map(int,sys.stdin.readline().split()))
AminB = set()
BminA = set()

for a in A_arr :
  AminB.add(a)
for b in B_arr :
  if b in AminB :
    AminB.remove(b)

for b in B_arr :
  BminA.add(b)
for a in A_arr :
  if a in BminA :
    BminA.remove(a)
print(len(AminB) + len(BminA))
