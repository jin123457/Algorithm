import sys

input = sys.stdin.readline

KP,SP,M = input().rstrip().split()
M = int(M)
spelling = ['A','B','C','D','E','F','G','H']
mvs = {
  'R' : (1,0),
  'L' : (-1,0),
  'B' : (0,-1),
  'T' : (0,1),
  'RT' : (1,1),
  'LT' : (-1,1),
  'RB' : (1,-1),
  'LB' : (-1,-1),
}
for i in range(len(spelling)) :
  if list(KP)[0] == spelling[i] :
    KP = [i + 1,int(list(KP)[1])]

for i in range(len(spelling)) :
  if list(SP)[0] == spelling[i] :
    SP = [i + 1,int(list(SP)[1])]


for _ in range(M) :
  A = input().rstrip()
  if (1 > KP[0] + mvs[A][0] or KP[0] + mvs[A][0] > 8) or (1 > KP[1] + mvs[A][1] or KP[1] + mvs[A][1] > 8) : continue

  if KP[0] + mvs[A][0] == SP[0] and KP[1] + mvs[A][1] == SP[1] :
    if (1 > SP[0] + mvs[A][0] or SP[0] + mvs[A][0] > 8) or (1 > SP[1] + mvs[A][1] or SP[1] + mvs[A][1] > 8) : continue
    else :
      SP[0] += mvs[A][0]
      SP[1] += mvs[A][1]
  KP[0] += mvs[A][0]
  KP[1] += mvs[A][1]

print(f"{spelling[KP[0] - 1]}{KP[1]}")
print(f"{spelling[SP[0] - 1]}{SP[1]}")