import sys

input = sys.stdin.readline

def is_prime(nm) :
  if nm == 0 or  nm == 1 : return False 
  for j in range(2,int(nm**0.5)+1) :
    if nm % j == 0:
      return False
  return True

T = int(input())

for _ in range(T) :
    N,M = input().split()
    K = M
    arr = []
    if is_prime(int(M)) :
        is_happy = False
        while True :
            if K == "1" : 
                is_happy = True
                arr.append(K)
                break
            elif K in arr : 
                arr.append(K)
                break
            nm = 0
            
            for h in list(K) :
                nm += int(h) ** 2
            arr.append(str(K))
            K = str(nm)
        print(N,M,end=" ")
        if is_happy :
            print('YES')
        else :
            print('NO')
    else :
        print(N,M,'NO')