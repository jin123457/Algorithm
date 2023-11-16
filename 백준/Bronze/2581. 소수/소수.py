M = int(input()) # 최소값을 입력 받기
N = int(input()) # 최대값을 입력 받기
arr = [] # 정답을 담을 배열 초기화

# 최소값 부터 최대값까지 for문을 돌리면서 소수를 찾는다.
for i in range(M,N + 1) :
  if i == 1 : continue # 1일 경우 1은 소수가 아니기에 넘겨준다.
  result = True # 소수를 판별할 변수 선언
  # 소수를 판별하는 for문 i % j를 하면서 하나라도 i % j == 0이 있을 경우 그 수는 소수가 아니다.
  for j in range(2,i) :
    if i % j == 0 :
      result = False
  # 소수인 것을 배열에 담아준다.
  if result :
    arr.append(i)
# 배열에 아무것도 담겨져 있지 않을 경우 -1을 출력하고 아닐 경우, 모든 수를 더한 값과 최소값을 출력한다.
if len(arr) <= 0 :
  print(-1)
else :
  print(sum(arr))
  print(min(arr))