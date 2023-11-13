N = int(input())
i = 1
j = 1
while True :
  if N <= i : break
  i += 6 * j
  j += 1
print(j)