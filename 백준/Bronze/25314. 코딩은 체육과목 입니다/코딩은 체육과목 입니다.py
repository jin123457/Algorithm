import sys

longCnt = int(sys.stdin.readline())
srtTotal = ""

for i in range(1,longCnt,4) :
  srtTotal += "long "

print(srtTotal + "int")