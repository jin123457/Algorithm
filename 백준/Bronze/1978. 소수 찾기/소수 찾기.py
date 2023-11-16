N = int(input())
A = list(map(int,input().split())) # 배열로 입력을 받는다.
count = 0 # 소수의 개수를 담을 변수 초기화

# 배열을 하나씩 꺼낸다.
for M in A : 
  if M == 1 : continue # 1은 소수가 아니므로, 넘어간다.

  result = True # 소수를 판별하기 위한 변수
  # 2부터 M -1까지 돌면서 소수 판별한다.
  for X in range(2,M) :
    # M % X가 딱 떨어지게 되면 소수가 아니다.
    if M % X == 0 :
      result = False
  # 위의 for문을 돌면서 한 번도 소수가 없으면 count + 1을 해준다.
  if result :
    count += 1

print(count)