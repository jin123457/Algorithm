import sys

input = sys.stdin.readline

N,M = map(int,input().split())
arr = list(map(int,input().split()))
sum_arr = [0] * (N + 1)
sum_arr[1] = arr[0]
ans = []

for i in range(2,N + 1) :
    sum_arr[i] = sum_arr[i - 1] + arr[i - 1]

for i in range(N - M + 1) :
    ans.append(sum_arr[i + M] - sum_arr[i])

maxnm = max(ans)

if maxnm == 0 :
    print('SAD')
else :
    print(maxnm,ans.count(maxnm),sep="\n")