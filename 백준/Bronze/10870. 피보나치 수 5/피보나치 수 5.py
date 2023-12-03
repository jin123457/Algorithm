N = int(input())
arr = [0,1]
def Fibonacci(nm,arr) :
  if nm == 0 : return arr
  else :
    arr.append(arr[-1]+arr[-2])
    nm -= 1
    return Fibonacci(nm,arr)
  
print(Fibonacci(N,arr)[-2])