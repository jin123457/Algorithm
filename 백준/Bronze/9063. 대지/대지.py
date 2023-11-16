N = int(input()) # 좌표의 개수를 받아온다.
coordinate_value = [list(map(int,input().split())) for _ in  range(N)] # 좌표의 개수대로 배열에 입력을 받는다.
w_arr = [] # 좌표에 x 값을 담을 배열 초기화
h_arr = [] # 좌표에 y 값을 담을 배열 초기화

# coordinate_value 배열에 있는 값들을 coordinate 담아서 하나씩 빼준다.
for coordinate in coordinate_value :
  x,y = coordinate # coordinate의 값을 각각 x,y에 담아준다.
  w_arr.append(x) # w_arr 배열에 x 값을 넣어준다.
  h_arr.append(y) # h_arr 배열에 y 값을 넣어준다.

# 답은 직사각형의 넓이를 구하는 식인 (w_arr 배열에서 제일 큰 값 - 제일 작은 값) * (h_arr 배열에서 제일 큰 값 - 제일 작은 값) 으로 계산해준다.
# w_arr 배열과 h_arr 배열에서 제일 큰 수와 제일 작은 수를 빼는 이유는 한 변의 길이를 알 수 있기 때문이다.
print((max(w_arr) - min(w_arr)) * (max(h_arr) - min(h_arr)))