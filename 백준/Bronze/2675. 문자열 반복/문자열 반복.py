N = int(input())
str_arr = [list(map(str,input().split())) for _ in range(N)]

for arr in str_arr :
  for i in range(len(arr[1])) :
    print(arr[1][i] * int(arr[0]), end="")
  print()