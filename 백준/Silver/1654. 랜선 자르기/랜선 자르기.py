import sys

input = sys.stdin.readline

def binary_search(A,T) :
  S,E = 1,max(A)
  lan = []
  max_lan = 0
  while S <= E :
    mid = (S + E) // 2
    total = 0

    for a in A :
      if a >= mid :
        total += (a // mid)

    if total >= T :
      lan.append(mid)

    if total >= T :
      S = mid + 1
    else :
      E = mid - 1
  if len(lan) == 0 :
    max_lan = 1
  else :
    max_lan = max(lan)
  return max_lan
K,N = map(int,input().split())
arr = [int(input()) for _ in range(K)]

print(binary_search(arr,N))