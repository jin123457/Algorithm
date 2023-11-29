import sys

input = sys.stdin.readline

limit = 1000001
prime_list = [i for i in range(limit)]
prime_list[0] = 0
prime_list[1] = 0

for i in range(4,limit,2) : prime_list[i] = 0
for i in range(3,limit,2) :
  for j in range(i * 2,limit,i) :
    if prime_list[j] :
      prime_list[j] = 0
      
T = int(input())

for _ in range(T) :
  N = int(input())
  count = 0

  for i in range(1,N // 2 + 1) :
    if prime_list[i] + prime_list[N - i] == N :
      count += 1
  print(count)
