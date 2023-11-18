import sys
N,M = map(int,sys.stdin.readline().split()) # 들어보지도 못 한 사람의 수는 N, 보지도 못한 사람의 수는 M이다.
arr = [sys.stdin.readline().rstrip() for _ in range(N + M)] # 사람들의 이름은 arr라는 배열 안에 담는다.
people_arr = set() # 들어보지도 못한 사람들의 정보는 people_arr에 담는다
ans = [] # 정답을 담을 배열
# for문은 arr에 길이만큼 돌린다.
for i in range(len(arr)) :
  # i가 N보다 작을 경우 people_arr에 arr[i]를 담는다. => 들어보지도 못한 사람들
  # i가 N보다 같거나 클경우는 people_arr에 arr[i]가 있는지 확인 후 정답 배열에 담는다.
  # => 보지도 못한 사람들이 들어보지도 못한 사람들인지 확인하고 듣보잡일 경우 정답배열에 담는다.
  if i < N :
   people_arr.add(arr[i])
  else :
    if arr[i] in people_arr :
      ans.append(arr[i])
print(len(ans)) # 듣보잡의 명수
# 듣보잡의 이름은 사전순으로 정렬 후 하나씩 출력한다.
for people in sorted(ans) :
  print(people)