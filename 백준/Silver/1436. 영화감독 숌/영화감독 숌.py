import sys

N = int(sys.stdin.readline()) # 몇 번째 시리즈인지 알아보는 자연수
ans = [] # 666이 들어가는 숫자를 담을 리스트
nm = 666 # 666이 들어가는 제일 작은 수는 666이니까 초기화 선언

# ans의 길이가 N보다 크거나 같을 때 멈추는 while문
while True :
  word = str(nm) # 666이 연속적으로 들어가는지 확인하기 위해, 숫자를 문자열로 치환한다.
  is_include = False # 666이 연속적으로 들어가는지를 알기위해 boolean형 초기화
  # for문을 돌면서 문자열을 슬라이싱 한다.
  for i in range(len(word)) :
    # i + 1를 한 이유는 slicing을 하면 해당 숫자보다 -1만큼 가져오기 때문에 + 3을 해줬다. 
    # 예) word[0:2] 일 경우, word의 0번째와 1번째만 가져온다. 
    # 우리가 원하는 것은 3자리 이므로 + 1를 시켜준다.
    # 슬라이싱 한 문자열이 666일시 is_include를 true로 변환한다.
    if word[i:i + 3] == "666" :
      is_include = True
  # is_include가 true일 때 해당 문자열을 배열에 넣어준다.
  if is_include :
    ans.append(word)
    
  nm +=1 # 숫자를 하나씩 증가시켜준다.
  # 리스트의 길이가 N보다 크거나 같으면 해당 문자열을 출력하고 종료한다.
  if len(ans) >= N :
    print(word)
    break