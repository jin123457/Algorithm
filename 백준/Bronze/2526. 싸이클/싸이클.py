import sys

input = sys.stdin.readline

N,M = map(int,input().split()) # 두 수를 공백 간격으로 나뉘어서 가지고 온다.
arr = [] # 나머지를 담을 배열 선언
cycle_arr = [] # 사이클이 되는 수를 담을 배열
k = N # 처음 K는 N * N이고, 그 다음 부터는 나머지 * N이기 떄문에 N을 k에 초기화 선언해준다. 

while True :
  k *= N # k * N을 k에 선언
  k %= M # k % M을 k에 선언
  # ans 배열 안에 k가 없을 경우 배열에 넣어주고 있을 경우 cycle_arr에 넣어준다.
  if k not in arr :
    arr.append(k)
  else :
    cycle_arr.append(k)
  # 사이클 배열 안에 있는 수가 k라면 while문 종료
  if k in cycle_arr :
    break
# 배열 안에 있는 숫자 중 언제부터 사이클이 반복될지 모르는 상황이기 때문에,
# 배열의 길이 - arr배열 안에 cycle_arr[0]의 인덱스를 빼주고 출력한다.
print(len(arr) - arr.index(cycle_arr[0]))