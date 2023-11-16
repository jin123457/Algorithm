side_arr = [] # 정답을 담을 배열 초기화
# arr 배열에 0,0,0이 들어오기 전까지 무한루프
# side_arr에 각각의 배열을 담아준다.
while True :
  arr = list(map(int,input().split()))
  if sum(arr) == 0 : break
  side_arr.append(arr)
# side_arr 배열을 담은 sides 배열을 하나씩 꺼내준다 예) [7,7,7]
for sides in side_arr :
  max_nm = max(sides) # 베열의 최고 값을 구한다.
  sum_nm = sum(sides) - max(sides) # 베열의 최고 값 - 나머지의 값을 구한다.
  same_count = 0 # 배열의 같은 값이 몇 개 있는지 알아보기 위한 변수 선언

  # for문을 돌면서 배열의 같은 값이 몇 개 있는지 개수를 알아본다.
  for j in sides :
    if same_count < sides.count(j) :
      same_count = sides.count(j)
  # 한 변의 값이 나머지 두 변의 값이랑 같거나 크면 삼각형이 될 수 있는 기준이 안되서 'Invalid' 출력
  # 같은 변이 3개면 정삼각형이므로 'Equilateral' 출력
  # 같은 변이 2개면 이등변삼각형이므로 'Isosceles' 출력
  # 같은 변이 1개도 없으면 그냥 삼각형이므로 'Scalene' 출력
  if max_nm >= sum_nm:
      print('Invalid')
  elif same_count == 3 :
    print('Equilateral')
  elif same_count == 2 :
      print('Isosceles')
  else :
      print('Scalene')