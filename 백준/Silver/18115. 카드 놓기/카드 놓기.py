import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
mv = list(map(int,input().split()))
ans = deque()
for i in range(1, N  + 1) :
   tec = mv.pop()
   if tec == 1 :
      ans.appendleft(i)

   if tec == 2 :
      if len(ans) > 1 :
         ans.insert(1,i)
      else :
         ans.append(i)

   if tec == 3 :
      ans.append(i)

print(*ans)