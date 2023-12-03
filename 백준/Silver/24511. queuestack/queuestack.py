from collections import deque

N = int(input())
arr = deque()
M = list(map(int,input().split()))
J = list(map(int,input().split()))
K = int(input())
G = list(map(int,input().split()))

ans = []
count = 0

for i in range(N) :
  if M[i] == 0 :
    arr.append(J[i])
    count += 1
    
if count > 0 :
  for g in G :
    arr.appendleft(g)

  for j in range(len(arr) -1,len(arr)-K - 1,-1):
    ans.append(str(arr[j]))
else :
  for g in G :
    ans.append(str(g))
    
print(" ".join(ans[:K]))