import sys

input = sys.stdin.readline

def binary_search(A,T) :
  S,E = 0,len(A) - 1
  is_find = False
  while S <= E :
    mid = (S + E) // 2

    if A[mid] == T : 
      is_find = True
      break

    if A[mid] < T :
      S = mid + 1
    else :
      E = mid - 1

  return is_find

while True :
  N,M = map(int,input().split())
  if N == 0 and M == 0 : break 
  A = list(int(input()) for _ in range(N))
  B = list(int(input()) for _ in range(M))
  ans = 0
  for b in B :
    if binary_search(A,b) : ans += 1
    
  print(ans)