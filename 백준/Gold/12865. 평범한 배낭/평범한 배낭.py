import sys

input = sys.stdin.readline

N,K = map(int,input().split())
stuff = [[0,0]]
bag = [[0] * (K + 1) for _ in range(N + 1)]
for _ in range(N) :
   W,V = map(int,input().split())
   stuff.append([W,V])

for i in range(1,N + 1) :
   w,v = stuff[i]
   for j in range(1,K + 1) :
      if j < w :
         bag[i][j] = bag[i - 1][j]
      else :
         bag[i][j] = max(bag[i - 1][j - w] + v , bag[i - 1][j])
print(bag[N][K])