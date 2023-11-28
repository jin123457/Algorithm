import sys

input = sys.stdin.readline

N,M = map(int,input().split())
arr = [list(map(str,input())) for _ in range(N)]
left_node = []
right_node = []
find_left = False
find_right = False

for i in range(N) :
  for j in range(M) :
    if arr[i][j] == "#" :
      left_node.append(i + 1)
      left_node.append(j + 1)
      find_left = True
      break
  if find_left : break

for i in range(N - 1, -1, -1) :
  for j in range(M - 1, -1, -1) :
    if arr[i][j] == "#" :
      right_node.append(i + 1)
      right_node.append(j + 1)
      find_right = True
      break
  if find_right : break

mid = [(left_node[0] + right_node[0]) // 2,(left_node[1] + right_node[1]) // 2]

if arr[left_node[0] - 1][mid[1] - 1] == "." :
  print('UP')
elif arr[mid[0] - 1][left_node[1] - 1] == "." :
  print('LEFT')
elif arr[right_node[0] - 1][mid[1] - 1] == "." :
  print('DOWN')
else:
  print('RIGHT')
