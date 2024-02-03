import sys

input = sys.stdin.readline

N,M = map(int,input().split())
MP = [0,0]
P = 0
MS = 0

for i in range(N) :
   T,D = input().rstrip().split()

   if P == 0 :
      MP[0] += int(T) - MS
   if P == 1 :
      MP[1] -= int(T) - MS
   if P == 2 :
      MP[0] -= int(T) - MS
   if P == 3 :
      MP[1] += int(T) - MS

   if D == "right" : P += 1
   elif D == "left" : P -= 1
   P %= 4
   MS = int(T)
   if N - 1 == i :
      if P == 0 :
         MP[0] += M - MS
      if P == 1 :
         MP[1] -= M - MS
      if P == 2 :
         MP[0] -= M - MS
      if P == 3 :
         MP[1] += M - MS

if N == 0 : MP[0] += M

print(*MP)