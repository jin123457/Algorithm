import sys

# 카운팅 정렬 counting sort
N = int(sys.stdin.readline()) # 입력 받고자 하는 자연수의 개수
C = [0] * 10001 # 입력에 최대한 수를 미리 0으로 리스트를 초기화
# for문을 N만큼 돌면서 input을 받고, input을 인덱싱으로 넣어 +1을 시켜준다.
# 예) input = 1,  C[input] +=1 이런식으로 인덱싱을 input에 담아 +1을 시켜 카운팅을 해준다.
for _ in range(N) :
  C[int(sys.stdin.readline())] += 1
# for문을 입력에 최대한 수만큼 다시 돌면서 0이 아닌 숫자를 찾는다.
# C[i]가 0 보다 클시 for문을 다시 돌면서 i를 출력해준다.
for i in range(10001) :
  if C[i] != 0 :
    for _ in range(C[i]) :
      print(i)