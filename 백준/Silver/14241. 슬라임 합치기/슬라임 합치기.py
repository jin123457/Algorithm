import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
slime_plus = 0
score = 0
for i in range(1,N) :
   if i == 1 :
      slime_plus += A[i - 1] + A[i]
      score += A[i - 1] * A[i]
   else :
      score += slime_plus * A[i]
      slime_plus += A[i]

print(score)