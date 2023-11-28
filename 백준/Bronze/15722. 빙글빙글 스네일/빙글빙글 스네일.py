import sys

input = sys.stdin.readline

N = int(input())
i = 0
j = 1
ans = [0,0]
while True :
  if i == N : break
  x,y = ans
  for m in range(2) :
    if i == N : break
    for k in range(j) :
      if i == N : break
      if j == 1 :
        if m == 0 :
          y += 1
        elif m == 1 :
          x += 1
      elif j % 2 != 0 :
        if m == 0 :
          y += 1
        elif m == 1 :
          x += 1
      else :
        if m == 0 :
          y -= 1
        elif m == 1 :
          x -= 1
      ans = [x,y]
      i += 1
  j += 1

ans = map(str,ans)
print(" ".join(ans))