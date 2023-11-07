H,M = map(int,input().split())

if H == 0 :
  H = 24

if M > 45 :
  hour = H
  minute = M - 45
elif M == 45 :
  hour = H
  minute = 0
else :
  minute = M + 15
  if minute == 60 :
    hour = H
    minute = minute
  else :
    hour = H - 1
    minute = minute
if hour > 24 :
  hour = hour - 24
elif hour == 24 :
  hour = 0
print(str(hour) + " " + str(minute))