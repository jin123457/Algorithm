import sys

input = sys.stdin.readline

N = int(input()) # 주문을 하는 사람의 수
arr = [int(input()) for _ in range(N)] # 사람들이 팁을 주려고 하는 금액 리스트
arr.sort(reverse=True) # 최대값을 알아야 하기 때문에 팁을 많이 주는 사람을 앞으로 정렬시킨다.
order = 1 # 주문을 받는 순서 초기화
tip_arr = [] # 팁을 받을 수 있는 사람들이 주는 팁 리스트
# for문을 돌면서 팁의 금액을 가지고 온다.
# 팁은 원래 주려고 했던 금액 - (순서 - 1) 이다.
# 팁이 양수일 경우에만 tip_arr에 넣어주고, for문이 끝날 때 순서를 하나 늘려준다.
for i in arr :
  tip = i - (order - 1)
  if tip > 0 :
    tip_arr.append(tip)
  order += 1
# 배열에 담긴 수를 모두 더한 다음 출력해준다.
print(sum(tip_arr))