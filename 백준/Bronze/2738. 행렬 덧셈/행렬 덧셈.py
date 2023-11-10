N,M = map(int,input().split())
first_arr = [list(map(int,input().split())) for _ in range(N)]
second_arr = [list(map(int,input().split())) for _ in range(N)]

for i in range(N) :
  for j in  range(M) :
    print(first_arr[i][j] + second_arr[i][j], end=" ")
  print()