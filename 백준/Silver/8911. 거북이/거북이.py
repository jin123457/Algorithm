import sys

input = sys.stdin.readline

N = int(input())
arr = [input().rstrip() for _ in range(N)]
ans = []
for i in range(N):
  d = 0
  dire = [0, 0]
  min_r = max_r = min_c = max_c = 0
  for j in list(arr[i]):
    if j == 'F':
      if d == 0:
        dire[0] -= 1
        min_r = min(min_r, dire[0])
      if d == 1:
        dire[1] += 1
        max_c = max(max_c, dire[1])
      if d == 2:
        dire[0] += 1
        max_r = max(max_r, dire[0])
      if d == 3:
        dire[1] -= 1
        min_c = min(min_c, dire[1])
    elif j == 'B':
      if d == 0:
        dire[0] += 1
        max_r = max(max_r, dire[0])
      if d == 1:
        dire[1] -= 1
        min_c = min(min_c, dire[1])
      if d == 2:
        dire[0] -= 1
        min_r = min(min_r, dire[0])
      if d == 3:
        dire[1] += 1
        max_c = max(max_c, dire[1])
    elif j == 'L':
      d -= 1
      d %= 4
    elif j == 'R':
      d += 1
      d %= 4
  row = abs(max_r - min_r)
  col = abs(max_c - min_c)
  ans.append(str(row * col))
print("\n".join(ans))