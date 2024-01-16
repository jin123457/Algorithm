import sys

input = sys.stdin.readline

N = int(input()) # 배열의 길이
A = list(map(int,input().split())) # 기본 배열
dp = [1] * N # dp 배열 초기화 1로 초기화 하는 이유는 숫자가 하나라도 있으면 0이 아니라 1이기 때문에

# 1. 기본 배열 만큼 for문 돌리기
# 2. 0 ~ (i - 1) 만큼 돌리기 (찾고 있는 배열 이전의 개수만큼)
for i in range(len(A)) :
  for j in range(0,i) :
    # 3. 현재 숫자보다 작은 수만 조건에 들어간다.
    if A[i] > A[j] :
      # 현재 dp배열에 들어갈 수는 max(기본값,이전 값들 중에 제일 큰 수 + 1)
      dp[i] = max(dp[i],dp[j] + 1)
# dp배열 안에 제일 큰 수를 출력한다.
print(max(dp))