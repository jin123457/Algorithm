N = int(input())

def factorial(count,nm) :
  if nm == 0: return count
  else :
    count *= nm
    nm -= 1
    return factorial(count,nm)

def combination(r,n) :
  return factorial(1,n) // (factorial(1,r) * factorial(1,n-r))

for _ in range(N) :
  i,j = map(int,input().split())
  print(combination(i,j))