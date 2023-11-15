# 0,0 입력이 나오기 전까지 무한 반복
while True :
  ans = '' # 정답을 담을 변수 초기화
  A,B = map(int,input().split())
  if A == 0 and B == 0 : break # 0,0이 나오면 while문 끝내기

  # A가 B보다 클경우는 배수밖에 안되고, B가 A보다 클 경우 약수 밖에 안된다.
  # 배수와 약수를 구하는 식은 간단하다. (나머지 값 구하기)
  # 배수의 경우 큰 수 % 작은 수 값이 0 이면 큰 수는 작은 수에 배수이다.
  # 약수의 경우 큰 수 % 작은 수 값이 0 이면 작은 수는 큰 수에 약수이다.
  if A > B :
    if A % B == 0 : 
      ans = 'multiple'
  else : 
    if B % A == 0 :
      ans = 'factor'
  
  if not ans :
    print('neither')
  else :
    print(ans)