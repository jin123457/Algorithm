import sys

nm = int(sys.stdin.readline())

for i in range(1,nm + 1,1) :
  star = ""
  for j in range(nm,0,-1) :
    if i >= j :
      star += "*"
    else :
      star += " "
  print(star)