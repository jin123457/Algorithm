import sys

# 소수를 판별하는 함수 파라미터로 값을 받아서 2부터 nm의 루트 + 1만큼의 for문을 돈다.
# 돌 때마다 j의 값이 1씩 추가가 되고, 만약 파라미터 % j가 0이 하나라도 있을 경우 그 수는 소수가 아니다.
def is_prime(nm) :
    for j in range(2,int(nm ** 0.5) +1) :
        if nm % j == 0 :
            return False
        
    return True
ans = [] # 정답을 담을 리스트 선언
# 0이 나올때까지 계속해서 반복을 해야하므로 while문을 선택했다.
while True :
    N = int(sys.stdin.readline()) # N부터 2N까지의 소수를 몇 개인지 알아보기 위한 자연수를 N으로 받는다.
    count = 0 # N부터 2N까지의 소수가 몇 개인지 세는 변수 선언
    if N == 0 : break # 입력의 값이 0일 경우 while문은 종료된다.
    # 입력의 값이 1,2일 경우 for문을 돌지 못하기 때문에 위에서 소수의 개수 1을 출력한다.
    # 입력의 값이 1,2일 아닐 경우는 N + 1부터 2N + 1까지 돌면서 총 소수의 개수가 몇 개인지 파악한 후, for문이 끝날 때 개수를 정답 리스트에 담아준다.
    if N in [1,2] :
       ans.append(str(1))
    else :
        for i in range(N + 1,N * 2 + 1) :
            if is_prime(i) :
                count += 1
        ans.append(str(count))
        
# 정답배열을 한칸씩 내려주면서 출력한다.
print("\n".join(ans))