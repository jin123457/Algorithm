import sys

input = sys.stdin.readline

def check_student() :
    for _ in range(N ** 2) :
        s = list(map(int,input().split()))
        SN = s.pop(0)
        ST[SN] = s


def find_like(S) :
    LS = []
    max_blank = -1
    max_nm = -1
    for i in range(N) :
        for j in range(N) :
            if not CR[i][j] :
                blank_nm = 0
                total = 0
                for mr,mc in mv :
                    new_r = i + mr
                    new_c = j + mc
                    if 0 <= new_r < N and 0 <= new_c < N :
                        if CR[new_r][new_c] in ST[S] :
                            total += 1
                        if not CR[new_r][new_c] :
                            blank_nm += 1
                
                if max_nm == total and max_blank == blank_nm : continue
                elif max_nm <= total :
                    if  max_nm == total and max_blank > blank_nm : continue
                    LS = [(i,j)]
                    max_nm = total
                    max_blank = blank_nm
        
    return LS[0]

N = int(input()) #교실의 크키 및 학생 수를 알 수 있는 자연수
CR = [[0] * N for _ in range(N)] # 교실의 자리를 0으로 초기화
mv = [(1,0),(0,1),(-1,0),(0,-1)] # 상하좌우를 움직이는 편하게 정리
ST = {} # 학생의 정보를 정리하는 오브젝트
check_student() # 학생들의 정보를 한 번 초기화 시켜주는 함수



for i,S in enumerate(ST) :
    s_list = tuple(find_like(S))
    CR[s_list[0]][s_list[1]] = S

ans = 0
for i in range(N) :
    for j in range(N) :
        like_list = ST[CR[i][j]]
        cnt = 0
        for mr,mc in mv :
            new_r = i + mr
            new_c = j + mc
            if 0 <= new_r < N and 0 <= new_c < N :
                if CR[new_r][new_c] in like_list : cnt += 1

        if cnt == 1 :
            ans += 1
        elif cnt == 2 :
            ans += 10
        elif cnt == 3 :
            ans += 100
        elif cnt == 4 :
            ans += 1000

print(ans)