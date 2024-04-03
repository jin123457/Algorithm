def binary_search(A,T,S,E) :
  if S > E : return 0

  mid = (S + E) // 2

  if A[mid] == T :
    return 1
  elif A[mid] > T :
    return binary_search(A,T,S,mid - 1)
  else :
    return binary_search(A,T,mid + 1,E)

N = int(input())
arr = sorted(list(map(int,input().split())))
M = int(input())
find_arr = list(map(int,input().split()))

for f in find_arr :
  print(binary_search(arr,f,0,len(arr) - 1))