# 직사각형이 (0,0) 부터 (w,h)까지 있을 때 (x,y)에서 각 4변에서 제일 최소거리를 구하시오
# 입력 받을 값에 순서 x, y, w, h

arr = list(map(int,input().split()))
ans = [] # 각 변의 거리를 담을 배열 선언
# 첫번째 담을 값은 (x,y) 기준 왼쪽의 값
# 두번째 담을 값은 (x,y) 기준 아래의 값
# 세번째 담을 값은 (x,y) 기준 오른쪽의 값
# 네번째 담을 값은 (x,y) 기준 위의 값
ans.append(arr[0]) 
ans.append(arr[1])
ans.append(arr[2] - arr[0])
ans.append(arr[3] - arr[1])
# ans 배열의 값 중 가장 최소 거리를 나타내는 값을 출력한다.
print(min(ans))