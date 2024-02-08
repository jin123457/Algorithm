import sys

input = sys.stdin.readline

N,M = map(int,input().split())
postIt = []
ans = []
for _ in range(N) :
  action = input().rstrip().split()
  if action[0] == 'order' :
    postIt.append([int(action[1]),int(action[2])])

  if action[0] == 'sort' :
    postIt = sorted(postIt, key=lambda x:(x[1],x[0]))

  if action[0] == 'complete' :
    for i in range(len(postIt)) :
      if int(action[1]) == postIt[i][0] :
        postIt.pop(i)
        break
  if len(postIt) == 0 :
    ans.append(['sleep'])
  else :
    arr = []
    for i in range(len(postIt)) :
      arr.append(postIt[i][0])
    ans.append(arr)
    
for a in ans :
  print(*a)