N = int(input())
for i in range(1,N) :
  print(" " * (N - i),end="")
  print('*' * (i + (i - 1)))

for i in range(N,0,-1) :
  print(" " * (N - i),end="")
  print('*' * (i + (i - 1)))