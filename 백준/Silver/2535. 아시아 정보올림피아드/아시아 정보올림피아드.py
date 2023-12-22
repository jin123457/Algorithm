N = int(input())
obj = list()
ans = list()
target = list()
for i in range(N) :
  cs,cn,score = map(int,input().split())
  obj.append((score,cs,cn))

sorte_A = sorted(obj,key=lambda x:x[0],reverse=True)

for i in range(len(sorte_A)) :
  if len(ans) == 3 : break

  if target.count(sorte_A[i][1]) == 2 : continue

  target.append(sorte_A[i][1])
  ans.append(f"{sorte_A[i][1]} {sorte_A[i][2]}")
  
print("\n".join(ans))