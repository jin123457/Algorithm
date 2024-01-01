import sys

input = sys.stdin.readline

N = int(input())
A = []
score = 0

for _ in range(N) :
   info = input().rstrip()
   if info != "0" : 

      nm,sc,tm = info.split()
      if int(tm) > 1 :
         A.append([sc,int(tm)])
      else :
         score += int(sc)

      if len(A) > 0 :
         A[-1][-1] -= 1

   else :
      if len(A) == 0 : continue
            
      A[-1][-1] -= 1

      if A[-1][-1] <= 0 :
         score += int(A[-1][0])
         A.pop()

print(score)