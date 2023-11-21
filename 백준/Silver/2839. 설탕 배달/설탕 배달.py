N = int(input())
ans = []
count = 0
for i in range(0,N + 1,3) :
  for j in range(0,N + 1,5) :
    if N == i + j :
      ans.append([i,j])

if len(ans) > 0 :
  count += ans[0][0] // 3
  count += ans[0][1] // 5
  print(count)
else :
  print(-1)