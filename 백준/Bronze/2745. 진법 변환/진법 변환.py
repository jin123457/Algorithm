B,N = map(str,input().split())
N = int(N)
i = 0
total = 0
for number in B[::-1] :
  total += ((N ** i) * int(number,N))
  i += 1

print(total)