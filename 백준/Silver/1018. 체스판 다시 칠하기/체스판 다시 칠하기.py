import sys

N,M = map(int,sys.stdin.readline().split()) # 세로의 개수는 N, 가로의 개수는 M으로 선언한다.
arr = [list(map(str,sys.stdin.readline())) for _ in range(N)] # 체스판을 2차원 배열로 받는다.
ans = [] # 정답을 담을 배열 선언
# x,y -7을 하는 이유는 -8을 하게되면 아예돌지 않을 수 있다.
for x in range(N -7):
  for y in range(M -7):
    w_count = 0 # W가 먼저 시작하는 체스판 중 틀린 개수를 알아내는 변수 선언
    b_count = 0 # B가 먼저 시작하는 체스판 중 틀린 개수를 알아내는 변수 선언
    for row in range(x,x+8) :
      for col in range(y,y+8) :
        # 짝수의 row와 짝수의 col이거나, 홀수의row와 홀수의 col이 w가 아니면 w_count +1을 해준다.
        # 그 반대에 경우는 b_count를 +1을 해준다.
        if row % 2 == 0 and col % 2 == 0 or row % 2 == 1 and col % 2 == 1 :
          if arr[row][col] != 'W' :
            w_count += 1
          else :
            b_count += 1
        else :
          if arr[row][col] != 'B' :
            w_count += 1
          else :
            b_count += 1
    # 정답 배열에 각각의 답을 담아준다.
    ans.append(w_count)
    ans.append(b_count)
# 정답에 배열의 값 중 제일 최소값을 출력한다.
print(min(ans))