import sys

input = sys.stdin.readline

N = input()
count = 0
for i in range(1,int(N) + 1) :
  if i < 100 :
    count += 1
  else :
    nm = str(i)
    if int(nm[1]) - int(nm[0]) == int(nm[2]) - int(nm[1]) :
      count += 1
      
print(count)