side_arr = list(map(int,input().split())) # 변들을 side_arr 배열에 담아준다.

side_count = 0 # 같은 변이 몇 개인지 알아보기 위한 변수 초기화

# for문을 돌면서 같은 변이 몇 개인지를 파악한다.
for side in side_arr :
  if side_count < side_arr.count(side) :
    side_count = side_arr.count(side)
# 같은 변이 3개이면 변의 총합을 구해준다.
# 같은 변이 3개보다 적을 시 총합을 제외한 나머지 값 + 총합을 제외한 나머지 값 - 1을 해주면 최대 둘레를 알 수 있게된다.
if side_count == 3:
  print(sum(side_arr))
else :
  if side_arr[0] + side_arr[1] > side_arr[2] and side_arr[0] + side_arr[2] > side_arr[1] and  side_arr[1] + side_arr[2] > side_arr[0] :
    print(sum(side_arr))
  else :
    max_nm = max(side_arr)
    sum_nm = sum(side_arr) - max_nm

    print(sum_nm + (sum_nm - 1))