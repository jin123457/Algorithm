import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
room = [1 for _ in range(N)]

if M == 0 : print(N)
else :
   for _ in range(M) :
      S,E = map(int,input().split())
      for i in range(S,E) :
         if room[i] == 0 : continue
         room[i] = 0

   print(sum(room))