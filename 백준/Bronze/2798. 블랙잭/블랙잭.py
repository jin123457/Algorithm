N,M = map(int,input().split()) # 입력 받을 개수와 합의 최대치를 입력 받는다.
arr = list(map(int,input().split())) # 합을 구할 숫자들을 배열에 담는다.
total = 0 # 숫자 3개에 총합을 담아줄 변수 초기화

# for문 세번을 돌린다. 3가지 카드합의 경우의 수를 알아야 하기 때문이다.
for i in range(N) :
  for j in range(i + 1,N) :
    for k in range(j + 1,N) :
      sum_nm = arr[i] + arr[j] + arr[k] # 각각의 카드의 수를 더해준다.
      # 3가지 카드 수의 합이 기존 total보다 높고, 합의 값이 합의 최대치를 넘어가지 않을 경우에만 total을 sum_nm 값으로 교체해준다.
      if sum_nm <= M and sum_nm > total :
        total = sum_nm
        
print(total)