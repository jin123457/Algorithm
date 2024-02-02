MT = list(map(int,input().split()))
YT = list(map(int,input().split()))
MS = YS = 0
is_win = False
for i in range(9) : 
  MS += MT[i]
  if MS > YS :
    is_win = True
    break
  YS += YT[i]

if is_win : print('Yes')
else : print('No')