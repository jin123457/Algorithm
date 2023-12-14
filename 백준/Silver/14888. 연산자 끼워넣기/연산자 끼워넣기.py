import sys

input = sys.stdin.readline

def dfs(n,sm,add,sub,mul,div) :
    global mn,mx # 최소값과 최대값은 계속 갱신을 해줘야 하기 때문에 global로 가지고 온다.
    # n이 N과 같아졌을 때 최소 값과 최대값을 갱신해준다.
    if n == N :
        mn = min(mn,sm)
        mx = max(mx,sm)
        return
    
    if add > 0 :
        # add가 1이상일 때, 재귀를 호출한다.
        # 인자를 (n + 1로 인덱스 하나 이동, 기존 값의 현재값을 더하기, 더하기 숫자 - 1, 빼기, 곱하기, 나누기)
        dfs(n + 1,sm + A[n],add-1,sub,mul,div)
    if sub > 0 :
        # sub 1이상일 때, 재귀를 호출한다.
        # 인자를 (n + 1로 인덱스 하나 이동, 기존 값의 현재값을 빼기, 더하기, 빼기 숫자 - 1, 곱하기, 나누기)
        dfs(n + 1,sm - A[n],add,sub-1,mul,div)
    if mul > 0 :
        # mul 1이상일 때, 재귀를 호출한다.
        # 인자를 (n + 1로 인덱스 하나 이동, 기존 값의 현재값을 곱하기, 더하기, 빼기, 곱하기 숫자 - 1, 나누기)
        dfs(n + 1,sm * A[n],add,sub,mul-1,div)
    if div > 0 :
        # div 1이상일 때, 재귀를 호출한다.
        # 나눌 때 실수가 나올 수 있기 때문에, int로 감싸준다.
        # 인자를 (n + 1로 인덱스 하나 이동, 기존 값의 현재값을 나누기, 더하기, 빼기, 곱하기, 나누기 숫자 - 1)
        dfs(n + 1,int(sm / A[n]),add,sub,mul,div-1)

N = int(input()) # 숫자들을 담을 리스트의 길이
A = list(map(int,input().split())) # 숫자들을 담고있는 리스트
add,sub,mul,div = map(int,input().split()) # 더하기, 빼기, 곱하기, 나누기를 담고 있는 리스트
# 최소, 최대 값이 각각 -10억 이상 10억 이하 이기 때문에
mn = int(1e9) # 최소 값의 초기 값은 최대 값으로 설정해준다.
mx = -int(1e9) # 최대 값의 초기 값은 최소 값으로 설정해준다.
# 함수호출 인자는 각각 A의 인덱스, A의 처음 값, 더하기 수, 빼기 수, 곱하기 수, 나누기 수이다.
dfs(1,A[0],add,sub,mul,div)
# 정답을 한칸씩 내려서 출력한다.
print(mx, mn, sep="\n")