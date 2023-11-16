angle_arr = [int(input()) for _ in  range(3)] # 삼각형의 각들을 angle_arr 배열에 담는다.
is_Equilateral = False # 정삼각형일 경우 변수 초기화
is_Isosceles = False # 이등변삼각형일 경우 변수 초기화

# 세각의 합이 총 180일 때와 아닐 때로 조건식을 나눈다. 
# 아닐 경우 Error를 출력
if sum(angle_arr) == 180 :
  # 두 번 for문을 돌리면서 각각 각을 비교한다.
  for i in range(len(angle_arr)) :
    for j in range(i + 1, len(angle_arr)) :
      # 각이 같은 것이 있으면서 같은 각이 60일 경우는 정삼각형
      # 각이 같은 것이 있으면서 같은 각이 60이 아닐 경우 이등변삼각형
      # 각이 같은 것이 하나도 없으면 그냥 삼각형
      if angle_arr[i] == angle_arr[j] and angle_arr[i] == 60 :
        is_Equilateral = True
      elif angle_arr[i] == angle_arr[j] :
        is_Isosceles = True

  if is_Equilateral :
    print('Equilateral')
  elif is_Isosceles :
    print('Isosceles')
  else :
    print('Scalene')
    
else :
  print('Error')