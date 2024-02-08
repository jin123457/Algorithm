import sys

input = sys.stdin.readline

P,M = map(int,input().split())
room = []

for _ in range(P) :
  L,N = input().rstrip().split()
  L = int(L)
  
  if len(room) == 0 :
    room.append([(L,N)])
  else :
    is_find = False
    for i in range(len(room)) :
      if room[i][0][0] + 11 > L and room[i][0][0] - 11 < L and len(room[i]) < M:
        is_find = True
        room[i].append((L,N))
        break
    if not is_find :
      room.append([(L,N)])

for r in room :
  if len(r) == M : 
    print('Started!')
  else :
    print('Waiting!')
  for p in sorted(r,key=lambda x:x[1]) :
    print(*p)