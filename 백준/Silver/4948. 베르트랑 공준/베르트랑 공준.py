import sys

prime_list = [1] * (123456 * 2 + 1)
prime_list[0] = 0
prime_list[1] = 0
ans = []
# 소수를 판별하는 함수 파라미터로 N값을 받아서 N + 1부터 N * 2 + 1만큼의 for문을 돈다.
# prime_list의 인덱스 값이 i가 되고, i가 0이 아닐 경우 다시 한 번 for문을 돌린다.
# 두번째 for문을
def is_prime(nm) :
    for i in range(nm + 1,nm * 2 + 1) :
        if prime_list[i] :
            for j in range(2,int(i**0.5) + 1) :
                if i % j == 0 :
                    prime_list[i] = 0
                    break
        
    return prime_list

# 0이 나올때까지 계속해서 반복을 해야하므로 while문을 선택했다.
while True :
    N = int(sys.stdin.readline()) # N부터 2N까지의 소수를 몇 개인지 알아보기 위한 자연수를 N으로 받는다.
    # 입력의 값이 0일 경우 while문을 빠져나온다.
    # 입력의 값이 0일 아닐 경우 is_prime 함수의 파라미터로 N을 넘겨주고 리턴 값으로 배열을 받는다.
    if N == 0 : 
        break
    else :
      ans.append(str(sum(is_prime(N)[N + 1:2*N + 1])))

print("\n".join(ans))