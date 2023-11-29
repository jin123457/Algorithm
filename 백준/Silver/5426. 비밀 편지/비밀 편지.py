import sys
input = sys.stdin.readline

N = int(input()) # 문자를 몇 개 받을건지에 대한 자연수

# N만큼 for문을 돌면서 문자열을 하나씩 가지고 온다.
for _ in range(N) : 
  word = '' # 해독한 문자열을 차례대로 담을 배열 선언
  password = input().rstrip() # 암호화된 문자열 받아오기
  word_avg = int(len(password) ** 0.5) # 문자열의 제곱 수를 알아오기
  # for문을 두번 돌면서 문자열을 하나하나 분리해서 접근한다.
  # 처음 for문은 평균값부터 -1씩해준다 그 이유는 제곱 수의 끝부터 처음에 시작하는 단어가 나오기 때문이다.
  # 두번째 for문은 위에서 받은 i 값부터 시작해 암호화된 문자열의 길이만큼 반복하고 word_avg의 수만큼 건너뛴다.
  # word 배열에 password[j]를 넣어주고 모든 for문이 돌았을 때 join으로 하나의 문자열로 출력한다.
  for i in range(word_avg -1,-1,-1) :
    for j in range(i,len(password),word_avg) :
      word += password[j]
  print(word)