N = input()
lenght = len(N)
N = int(N)
ans = []
for i in  range(1,int(lenght) * 9 + 1) :
  minus_nm = N - i
  total = minus_nm
  if minus_nm > 0 :
    for nm in str(minus_nm) :
      total += int(nm)
  if N == total:
    ans.append(minus_nm)
if len(ans) :
  print(min(ans))
else :
  print(0)