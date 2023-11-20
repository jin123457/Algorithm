import sys

N = list(map(int,sys.stdin.readline().split())) # 한 줄의 자연수 두개를 정수형으로 변환해주고 리스트로 넣어준다.
# 최소 공배수를 알아내는 함수선언
# 파라미터로 큰 값은 a, 작은 값은 b에 담아준다.
def LCM(a,b) :
  a,b = max_nm,min_nm # 최대 공배수를 구하기 위해서는 최대 공약수를 알아야 하므로, 기존에 큰 값과 작은 값은 따로 변수에 저장해둔다.
  # a % b 가 0이 될 때까지 계속 while문을 돌린다.
  # 0이 안될 시, 작은 값은 큰 값이 되면 나머지 값은 작은 값이 된다.
  while b > 0:
    a, b = b, a % b
  # 최대 공약수가 구해졌으면 위에 저장을 해두었던 큰 값, 작은 값을 곱합 값 나누기 최대공약수를 하면 최소 공배수를 알 수 있다.
  return (max_nm * min_nm) // a

# 두개의 값 중에 큰 값과 작은 값을 따로따로 저장한다.
max_nm = max(N)
min_nm = min(N)
# 가장 작은 값이 1일 경우는 최소 공배수가 무조건 큰 값이므로 출력해준다.
# 가장 작은 값이 1이 아닐경우, 최소 공배수를 구하는 함수에 return 값을 출력해준다.
if min_nm == 1 :
  print(max_nm)
else :
  print(LCM(max_nm,min_nm))