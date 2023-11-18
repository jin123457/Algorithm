N = input()
arr = set()
for i in range(len(N)) :
  arr.add(N[i])
  for j in range(i +1,len(N)):
    arr.add(N[i:j+1])
print(len(arr))