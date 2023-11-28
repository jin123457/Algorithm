import sys

input = sys.stdin.readline

N = int(input()) # 책상은 정사각형이고 각 변은 N이다.
arr = [list(map(int,input().split())) for _ in range(N)] # 학생과 교수님의 자리배치도를 2차원 배열로 집어 넣는다.
t_p = [] # 교수님의 자리 좌표
m_p = [] # 나의 자리 좌표
find_t = False # 교수님의 위치를 찾았는지 알 수 있는 변수 선언
find_m = False # 나의 위치를 찾았는지 알 수 있는 변수 선언
cnt = 0 # 교수님과 나와의 거리 안에 학생 수를 나타낼 변수 선언
t_m_between = 0 # 교수님과 나와 책상 간에 거리 초기화
# for문을 두번 돌면서 모든 자리배치도의 모든 곳을 다 둘러본다.
# 교수님의 위치를 찾았을 경우 t_p의 좌표를 담아주고, find_t를 True로 변환해준다.
# 나의 위치를 찾았을 경우 m_p의 좌표를 담아주고, find_m를 True로 변환해준다.
# find_t와 find_m가 모두 True일 때, for문을 더이상 돌 필요가 없으므로 강제 종료시킨다.
for i in range(N) :
  for j in range(N) :
    if find_t and find_m : break

    if arr[i][j] == 5 :
      t_p.append(i)
      t_p.append(j)
      find_t = True
    elif  arr[i][j] == 2 :
      m_p.append(i)
      m_p.append(j)
      find_m = True
  if find_t and find_m : break

t_m_between = int((((t_p[0] - m_p[0]) ** 2) + ((t_p[1] - m_p[1]) ** 2)) ** 0.5) # 책상간에 거리를 구하는 식이다. (문제에 나와있음)
# for문을 두 번 돌린다. 그 이유는,
# 첫번째는 교수님이 계시는 좌표와 나의 좌표 중 세로에서 가장 값이 작은 곳부터 가장 값이 큰 값까지 돈다.
# 두번째는 교수님이 계시는 좌표와 나의 좌표 중 가로에서 가장 값이 작은 곳부터 가장 값이 큰 값까지 돈다.
# 이렇게 두 번 돌게 되면 교수님과 나의 위치 안에 포함된 사각형까지만 for문이 돌게되고 그 안에 학생 수가 몇 명있는지를 알 수 있게된다.
for i in range(min(t_p[0],m_p[0]),max(t_p[0],m_p[0]) + 1) :
  for j in range(min(t_p[1],m_p[1]),max(t_p[1],m_p[1]) + 1) :
    if arr[i][j] == 1 :
      cnt += 1
      
# 학생의 수가 3명 이상이면서 교수님과 나와의 거리가 5 이상일 경우의 1을 출력하고, 아닐 경우는 0을 출력한다.
if cnt >= 3 and t_m_between >= 5 :
  print(1)
else :
  print(0)