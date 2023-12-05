N,M = map(int,input().split())
index = 0
arr = [i for i in range(1,N + 1)]
ans = []
i = M - 1
while len(arr) > 0 :
  index += (M -1)
  index = index % len(arr)
  ans.append(str(arr.pop(index)))
  
print("<",end="")
print(", ".join(ans),end="")
print(">")