import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
ans = []
is_payed = False
for i in range(M) :
   for j in range(N) :
      if i > 0 :
         A[j][i] += A[j][i - 1]

      if A[j][i] >= K :
         ans.append(j + 1)
         ans.append(i + 1)
         is_payed = True
         break

   if is_payed : break
print(*ans)      