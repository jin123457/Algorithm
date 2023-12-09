import sys
from collections import deque

input = sys.stdin.readline
N,M = map(int,input().split())
arr = [deque([0] * (N + 1)) for _ in range(N + 1)]
ans = []

for i in range(1,N + 1) :
  A = deque(map(int,input().split()))
  for j in range(1,N + 1) :
    arr[i][j] = A[j - 1] + arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1]

for _ in range(M) : 
  x1,y1,x2,y2 = map(int,input().split())
  ans.append(str(arr[x2][y2] - arr[x1 -1][y2] - arr[x2][y1-1] + arr[x1-1][y1-1]))
  
print("\n".join(ans))
