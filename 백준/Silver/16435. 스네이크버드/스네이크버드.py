import sys

N,M = map(int,sys.stdin.readline().split()) # 과일의 개수는 N, 뱀의 몸의 길이는 M으로 선언한다.
arr = list(map(int,sys.stdin.readline().split())) # 과일의 높이를 배열로 담는다.
arr.sort() # 과일의 높이를 배열로 담은 것을 작은순으로 정렬을 해준다.
snake_len = M # 뱀의 처음 몸의 길이

# for문을 과일의 개수만큼 돌면서 정렬된 배열보다 뱀의 몸의 길이가 크거나 같으면 뱀은 과일을 먹고 1만큼 길어진다.
for i in range(N) :
  if snake_len >= arr[i] :
    snake_len += 1
# 뱀의 몸의 길이를 출력한다.
print(snake_len)