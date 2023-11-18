import sys
input = sys.stdin.readline
N = int(input()) # 로그에 남아있는 정보에 개수
people_obj = set() # 사람들의 정보를 담을 set 선언

# for문을 N만큼 돌면서 people_obj 딕셔너리에 출근과 퇴근에 대한 기록을 넣는다.
for _ in range(N) :
  name,info = input().split() # 로그에 있는 사람들의 정보를 하나씩 가지고 온다.
  
  # 이름이 people_obj에 없을 경우는 출근에 대한 것을 알아보고 있을 경우는 퇴근에 대한 것을 알아본다. 
  if name not in people_obj :
    if info == "enter" :
      people_obj.add(name)
  else :
    if info == "leave" :
      people_obj.remove(name)
# 회사에 남아있는 사람들의 이름을 사전의 역순으로 하나씩 꺼내온다. 
people_obj = sorted(people_obj, reverse=True)
for name in people_obj :
  print(name)