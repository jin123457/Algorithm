N,K = map(int,input().split())
arr = [] # 약수를 담을 배열 초기화

# N의 수 만큼 반복문을 돌면서 약수인 경우 arr 배열에 담는다.
for i in range(1, N + 1) : 
  if N % i == 0 :
    arr.append(i)
# 배열의 길이가 K보다 수가 높거나 같을 경우 약수를 출력 아닐경우 0을 출력
if len(arr) >= K :
  print(arr[K - 1])
else :
  print(0)