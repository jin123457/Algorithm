coordinate_value = [list(map(int,input().split())) for _ in  range(3)] # 배열로 입력을 받는다.
w_arr = [] # 좌표에 x 값을 담을 배열 초기화
h_arr = [] # 좌표에 y 값을 담을 배열 초기화

# 배열애 담긴 각각의 x,y 값을 빼온다
for arr in coordinate_value :
  N,M = arr # 하나씩 빼온 x,y의 값을 각각 N,M에 따로따로 담는다.

  # w_arr 배열에 N이 없으면 배열에 넣고 있으면 뺴준다.
  if N not in w_arr :
    w_arr.append(N)
  else :
    w_arr.remove(N)

  # h_arr 배열에 M이 없으면 배열에 넣고 있으면 뺴준다.
  if M not in h_arr :
    h_arr.append(M)
  else :
    h_arr.remove(M)
    
# 남은 값들이 정답이 요구하는 답이므로, 출력해준다.
print(f"{w_arr[0]} {h_arr[0]}")