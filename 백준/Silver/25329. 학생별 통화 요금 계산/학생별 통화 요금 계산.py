import sys

input = sys.stdin.readline
# Math 함수를 안 쓰고 올림하는 법 -int(-value // 1)
N = int(input())
obj = {}
ans = {}
for _ in range(N) :
    time,name = input().rstrip().split()
    hour,minute = time.split(':')
    total = 0
    if int(hour) > 0 :
        total += int(hour) * 60
    if int(minute) > 0 :
        total += int(minute)
    if name not in obj :
        obj[name] = total
    else :
        obj[name] += total

for tel_info in obj :
    name = tel_info
    time = obj[tel_info]
    price = 0
    if time > 100 :
        price += 10
        price += -int(-((time - 100) / 50) // 1) * 3
    else :
        price += 10
    
    if name not in ans :
        ans[name] = price

for A in sorted(ans.items(),key=lambda x:(-x[1],x[0])) :
    print(*A)