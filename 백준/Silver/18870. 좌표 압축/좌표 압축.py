import sys

input = sys.stdin.readline
N = int(input()) # 입력받을 자연수의 개수
arr = list(map(int,input().split())) # 입력 받는 숫자들 공백 간격으로 한 줄로 이뤄져있고, 나눠져있다
nm_data = sorted(list(set(arr))) # 중복값을 없애주기 위해 set 안에 넣어주고 정렬을 해준다.
ans = [] # 정답을 담을 리스트 선언
nm_index_data = {} # 인덱스와 키를 같이 받는 딕셔너리 선언
# enumerate 내장함수를 이용하면 index와 value을 얻을 수 있다.
# 이렇게 정리해놓으면 밑에서 for문을 돌려서 딕셔너리에서 호출은 엄청 빠르게 가지고 올 수 있다.
for index, value in enumerate(nm_data) :
  nm_index_data[value] = index


# 입력받은 숫자들을 하나씩 꺼내오면서 정렬해둔 리스트에 인덱스를 알아와, 정답 리스트에 넣어준다.
for x in arr :
  ans.append(str(nm_index_data[x]))
  
# 리스트를 공백 간격으로 출력해준다.
print(" ".join(ans))