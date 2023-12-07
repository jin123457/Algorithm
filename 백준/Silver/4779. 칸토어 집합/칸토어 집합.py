import sys

def change_str(start,end,text) :
  global A

  if end - start == 1 : return 

  S = start + (end - start) // 3
  E = start + (end - start) // 3 * 2

  for i in range(S,E) :
    A[i] = ' '

  change_str(start,S,"start")
  change_str(E,end,"end")

for input in sys.stdin :
  T = int(input)
  A = ['-'] * (3 ** T)
  
  change_str(0,len(A),"")
  print("".join(A))