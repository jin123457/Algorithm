A,B,C = map(int,input().split())

if A == B and B == C :
  print(10000 + A * 1000)
elif A == B or B == C  or A == C :
  if A == B or B == C :
    print(1000 + B * 100)
  else :
    print(1000 + A * 100)
else :
  if A > B and A > C :
    print(100 * A)
  elif  A < B and B > C :
    print(100 * B)
  else :
    print(100 * C)