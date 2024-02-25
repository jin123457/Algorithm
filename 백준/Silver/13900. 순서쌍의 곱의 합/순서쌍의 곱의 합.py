import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
sum_nm = sum(arr) - arr[0]
total = 0
ans = 0

for i in range(N) :
  if i + 1 >= N :continue

  ans += (sum_nm - total) * arr[i]
  total += arr[i + 1]
print(ans)