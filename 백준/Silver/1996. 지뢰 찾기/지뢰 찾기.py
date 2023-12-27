import sys

input = sys.stdin.readline
T = int(input())
A = [list(map(str,input().rstrip())) for _ in range(T)]
mv = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
ans = [[] for _ in range(T)]

for i in range(T) :
  for j in range(T) :
    if A[i][j] != "." :
      ans[i].append("*")
    else :
      count = 0
      for new_r,new_c in mv :
        new_r += i
        new_c += j
        if 0 <= new_r < T and 0 <= new_c < T :
          if A[new_r][new_c] != "." :
            count += int(A[new_r][new_c])

      if count > 9 : count = "M"

      ans[i].append(str(count))
      
for i in ans :
  print(*i,sep="")