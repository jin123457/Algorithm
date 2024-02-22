import sys

input = sys.stdin.readline

N,M = map(int,input().split())
arr = sorted([int(input()) for _ in range(N)],reverse=True)
ans = 0

for i in range(len(arr)) :
  if arr[i] > M : continue
  ans += M // arr[i]
  M %= arr[i]
  
print(ans)