A,B = map(int,input().split())
nm = A # 길이를 구할 변수 초기화
length = 0 # 길이 초기화
answer = "" # 정답을 담을 문자열 초기화 (문자열로 담는 이유는 16진법으로 가면 숫자가 아니라 알파벳도 나오기 떄문이다.)

# 길이 구하기
while True : 
  # nm // B의 값이 0이 될 때 멈춘다.
  if nm // B <= 0 :
    length += 1
    break
  # 위의 조건에 걸리지 않을 시 길이를 하나 늘려주고, nm의 값을 A // B로 초기화 해준다.
  length += 1
  nm //= B

#길이 만큼 돌면서 B만큼 나눈다.
for i in range(length) :
  N = A % B # N이라는 변수에 A % B 담아주고 아래의 조건식으로 정답에 각각 담아준다.
  if N < 10 :
    answer += str(N)
  else :
    answer += chr(55 + N) # N이 10이 넘어갈 경우 숫자가 아니라, 알파벳으로 나오기 때문에 아스키코드를 이용해서 정답에 담아준다.
  A //= B # 정답을 담은 후, A // B를 다시 A에 담아준다.

print(answer[::-1])