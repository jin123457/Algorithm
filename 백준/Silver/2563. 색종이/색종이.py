N = int(input())
arr = [list(0 for _ in range(100)) for _ in range(100)]
position_arr = [list(map(int, input().split())) for _ in range(N)]
total = 0

def solution(position) :
  x,y = map(int,position)
  for i in  range(y - 1,(y - 1) + 10,1) :
    for j in range(x - 1,(x - 1) + 10,1) :
      arr[i][j] = 1

for position in position_arr :
  solution(position)

for find_x in arr :
  for find_y in find_x :
    if find_y == 1 :
      total += 1

print(total)