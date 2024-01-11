dp = [0] * 1000001
dp[:3] = [0,1,2]
for i in range(3,1000001) :
    if i >= 15746 :
        dp[i] = (dp[i - 1] + dp[i - 2]) % 15746
    else :
        dp[i] = dp[i - 1] + dp[i - 2]
N = int(input())

print(dp[N])