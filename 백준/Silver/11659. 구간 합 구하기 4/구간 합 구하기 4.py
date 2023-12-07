import sys

input = sys.stdin.readline
N,M = map(int,input().split())
arr = list(map(int,input().split()))
S = []
ans = []
for i in range(N + 1) :
  if i == 0 :
    S.append(0)
  else :
    S.append(arr[i - 1] + S[i - 1])

for _ in range(M) :
  i,j = map(int,input().split())
  ans.append(str(S[j] - S[i -1]))
  
print("\n".join(ans))