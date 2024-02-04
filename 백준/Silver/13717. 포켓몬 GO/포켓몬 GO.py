import sys

input = sys.stdin.readline

N = int(input())
obj = {}
for _ in range(N) :
  name = input().rstrip()
  need,current = map(int,input().split())
  time = 0
  while True :
    if need > current : break
    current -= need
    current += 2
    time += 1
  
  obj[name] = time
print(sum(obj.values()))
for i in obj :
  if obj[i] == max(obj.values()) :
    print(i)
    break