import sys

N,M = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
food_cnt = N
snake_len = M

for i in range(N) :
  if snake_len >= arr[i] :
    snake_len += 1

print(snake_len)