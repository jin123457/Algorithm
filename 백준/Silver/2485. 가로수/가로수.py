import sys

N = int(sys.stdin.readline()) # 현재 심어져있는 나무의 개수
arr = [int(sys.stdin.readline()) for _ in range(N)] # 거리에 현재 심어져 있는 나무의 위치의 수 예) 1m,3m,5m,7m
C = [] # 현재 심어져있는 나무들 사이의 간격들을 담는 리스트 선언

# 최대공약수를 알아내는 함수 (재귀함수)
def GCD(a,b) :
    if a % b == 0 :
        return b
    else :
        return GCD(b,a%b)
    
# for문을 arr길이 - 1만큼 돌면서 서로의 간격을 알아낸다.
# 예) 3 - 1 간격이 2가 되니까 C배열에 담아준다. => 이 과정을 계속해서 반복
for i in range(len(arr) -1) :
    C.append(arr[i + 1] - arr[i])

# C 리스트에 담겨져 있는 간격들의 모든 수의 최대공약수를 알아낸다.
# j == 0일 때는 C[j+1],C[j] 이렇게 첫번째 요소와 두번째 요소의 간격을 넣고 구하지만
# 그 다음부터는 세번째 요소와 첫번쨰 요소,두번째 요소의 최대공약수의 최대공약수를 구해줘야한다.
for j in range(len(C)) :
    if j == 0 :
        gcd = GCD(C[j+1],C[j])
    else:
        gcd = GCD(C[j],gcd)

# 리스트에서 마지막 요소 - 첫번째 요소를 해주면 거리의 길이를 알게되고
# 나누기 최대공약수를 해주면 몇 개의 나무가 심어져야 하는지를 알게된다. 
# 그 값에서 현재 심어져있는 나무의 개수를 빼주고 한 그루를 추가해줘야 현재 나무 몇 그루를 심어야하는지를 알게된다.
print(((arr[-1] - arr[0]) // gcd) - N + 1)