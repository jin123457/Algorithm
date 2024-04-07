import sys

input = sys.stdin.readline

def binary_search(A,T) :
  S,E = 1,max(A)
  money_arr = []

  while S <= E :
    mid = (S + E) // 2
    total = 0
    
    for a in arr :
      if a >= mid :
        total += mid
      else :
        total += a

    if T >= total :
      money_arr.append(mid)

    if T >= total :
      S = mid + 1
    else :
      E = mid - 1
    
  return max(money_arr)



N = int(input())
arr = list(map(int,input().split()))
K = int(input())

print(binary_search(arr,K))