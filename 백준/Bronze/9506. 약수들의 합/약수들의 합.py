while True :
  N = int(input())
  if N == -1 : break
  arr = []
  for i in range(1,N + 1) : 
    if N % i == 0 :
      arr.append(i)
  arr.pop()
  
  if N == sum(arr) :
    arr = map(str,arr)
    result = " + ".join(arr)
    print(f"{N} = {result}")
  else :
    print(f"{N} is NOT perfect.")