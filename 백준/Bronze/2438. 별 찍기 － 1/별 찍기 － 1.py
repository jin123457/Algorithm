import sys

nm = int(sys.stdin.readline())

for i in range(1,nm + 1,1) :
  star = ""
  for j in range(1,i + 1,1) :
    star += "*"
  print(star)