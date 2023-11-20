import sys

N = int(sys.stdin.readline()) # 문자열 개수
people_data = [] # 리스트 초기화 선언
# for문을 돌면서 입력을 받고, 공백을 사이로 두 데이터를 각각 age,name으로 변수에 담는다.
# people_data 안에 배열로 age와 name을 넣어서 people_data에 넣어준다. 예) [[age,name],[age,name],[age,name].....]
for _ in range(N) :
  age,name = sys.stdin.readline().split()
  people_data.append([age,name]) 

people_data.sort(key=lambda x : int(x[0])) # people_data 안 배열의 1번 인덱스로 정렬을 한다.
for people in people_data :
  # people 배열 안에 하나씩 빼주면서 출력해준다.
  # people[0] = name
  # people[1] = age
  print(f"{people[0]} {people[1]}")