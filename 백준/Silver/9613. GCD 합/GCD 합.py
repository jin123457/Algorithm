import sys

input = sys.stdin.readline

N = int(input()) # 줄의 개수
ans = [] # 정답을 담을 배열
# 최대 공약수를 알아보는 함수
# a % b == 0 일때는 b를 리턴, 아닐 경우는 b와 a%b로 다시 재귀
def GCD(a,b) :
  if a % b == 0 : 
    return b
  else :
    return GCD(b,a%b)
# N의 개수만큼 for문을 돌린다.
for _ in range(N) :
  arr = list(map(int,input().split())) # 배열 안에 줄을 공백 간격으로 나눈뒤 숫자형으로 배열에 다시 담는다.
  gcd_arr = [] # 최대공약수들을 담을 배열 선언
  # 모든 경우의 수를 확인해야하기 떄문에 for문을 두번 돌린다.
  # 배열의 첫번째 수는 몇 개의 수의 최대공약수를 알아볼건지에 대한 수이다.
  for i in range(1,arr[0] + 1) :
    for j in range(i + 1,arr[0] + 1) :
      gcd_arr.append(GCD(arr[i],arr[j])) # 최대공약수 배열에 최대공약수를 넣어준다.
  ans.append(sum(gcd_arr)) # 최대 공약수 배열을 더한 뒤, 정답 배열 안에 넣어준다.
ans = list(map(str,ans)) # 정답 배열안에 수를 join으로 출력하기 위해 모든 수를 sting으로 형변환 해준다.
# 배열을 한 줄 간격으로 출력한다.
print("\n".join(ans))
