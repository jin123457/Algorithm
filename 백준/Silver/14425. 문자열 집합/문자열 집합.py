import sys
input = sys.stdin.readline

N,M = map(int,input().split()) # 집합에 포함되어있는 문자열의 개수는 N, 집합에 포함되어있는지 알아보는 문자열들의 개수는 M
str_arr = [input() for _ in range(N + M)] # 문자열들을 배열 안에 넣는다.
str_obj = set() # set으로 집합에 포함되어있는 문자열을 담는다.
count = 0 # 두 번 이상인 집합에 포함되어있는 문자열의 개수를 저장할 변수 초기화

# for문을 돌면서 N보다 작은 것은 집합에 포함되어있는 기준 문자열을 넣고 나머지는 기준 문자열과 중복이 되는지 확인 후 중복이 되면 카운트 + 1을 시켜준다.
for i in range(N + M) :
  if N > i :
    str_obj.add(str_arr[i])
  else :
    if str_arr[i] in str_obj :
      count += 1
    
print(count)