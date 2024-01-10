N = int(input())
dp = [0] * (N + 1)
count = 0
for i in range(N + 1) :
  if i == 0 : continue
  if i == 1 or i == 2 : 
    dp[i] = 1
  else :
    count += 1
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[-1],count)