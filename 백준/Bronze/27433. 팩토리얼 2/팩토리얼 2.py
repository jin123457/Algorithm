N = int(input())

def Factorial(nm,count) :
  if nm == 0 : return count
  else :
    count *= nm
    nm -= 1
    return Factorial(nm,count)
  
print(Factorial(N,1))