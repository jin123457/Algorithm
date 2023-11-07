import sys

i = int(sys.stdin.readline())

for j in range(1,i + 1,1) :
  nm = sys.stdin.readline().split()
  print("Case #" + str(j) + ": " + str(nm[0]) + " + " + str(nm[1]) + " = " + str(sum(map(int,nm))))