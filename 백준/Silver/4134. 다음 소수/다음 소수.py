import sys

N = int(sys.stdin.readline()) # 몇 개의 자연수를 입력 받을건지에 대한 자연수 선언
# 소수를 판별하는 함수
# int(nm ** 0.5)의 뜻은 nm의 루트를 씌우는 것이다.
# 도는 수가 엄청나게 줄어듬 소수점이 있을 수 있어 int로 변환 후 + 1을 해준다.
# for문을 도는 과정 중에 나머지가 0인 것이 있으면 소수가 아니게 된다.
def isPrime(nm):
  for j in range(2,int(nm**0.5)+1) :
    if nm % j == 0:
      return False
  return True

# N만큼 for문을 돌면서 입력을 받는다.
for _ in range(N) :
  nm = int(sys.stdin.readline())
  # nm의 숫자가 0,1일 경우 다음 소수는 무조건 2이다.
  # 그 반대의 경우 nm부터 nm의 제곱 2 +1을 한 경우까지 검사를 한다.
  # 도는 과정 중 소수가 있을 경우 곧 바로 for문을 종료시킨다.
  if nm in [0,1] :
     print(2)
  else :
    for i in range(nm,(nm * nm) + 1):
      if(isPrime(i)):
        print(i)
        break