import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
T = int(input())
S = list(map(int,input().split()))
A = deque()
for i,v in enumerate(S) :

  if len(A) < N :
    is_in = False
    for j in range(len(A)) :
      if A[j][0] == v : 
        A[j][2] += 1
        is_in = True
        break

    if not is_in :
      A.append([v,i,1])

  else :
    is_in = False
    for j in range(len(A)) :
      if A[j][0] == v : 
        A[j][2] += 1
        is_in = True
        break

    if not is_in :
      A = deque(sorted(A,key=lambda x:(x[2],x[1])))
      A.popleft()
      A.appendleft([v,i,1])

ans = []
for a in A :
  ans.append(a[0])
print(*list(sorted(ans))) 