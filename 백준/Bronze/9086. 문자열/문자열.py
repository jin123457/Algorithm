N = int(input())
str_arr = [input() for _ in range(N)]

for str in str_arr :
  print(str[0], end="")
  print(str[-1])