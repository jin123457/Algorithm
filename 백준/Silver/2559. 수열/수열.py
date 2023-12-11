import sys

input = sys.stdin.readline

N,M = map(int,input().split()) # 배열의 크기는 N, 연속적으로 더할 숫자는 M에 넣어준다.
arr = list(map(int,input().split())) # 배열을 숫자형으로 변환 후 리스트를 정렬한다.
target = sum(arr[:M]) # 배열을 슬라이싱하여 M만큼의 배열로 잘라준 후, 더해준다.
ans = target # ans의 값을 처음 값으로 넣어준다. 다음의 수와 비교하기 위해 넣어준다.

for i in range(M,N) :
    target += arr[i] # 기준의 수의 다음수는 기존 값에 더해준다.
    target -= arr[i - M] # 기준의 수의 이전수는 기존 값에 빼준다.
    ans = max(ans,target) # 현재 값과 이전 값 중 더 큰 값을 ans의 넣어준다.
    
print(ans) # 정답을 출력한다.