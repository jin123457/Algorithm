H,M = map(int,input().split())
TM = int(input())

minute = M + TM
if minute >= 60 :
  hour = ((M + TM) // 60) + H
  minute = ((M + TM) % 60)
else :
  hour = H

if hour >= 24 :
  hour = hour -24
print(str(hour) + " " + str(minute))