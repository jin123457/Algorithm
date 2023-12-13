import sys

input = sys.stdin.readline

def combination() :
    checked = 0 # 이전 숫자가 어떤 것이 들어갔는지 알 수 있는 변수
    # ans 리스트의 길이가 M만큼 됐을 경우 공백을 간격으로 숫자를 출력해주고 return을 해준다.
    # 여기서 return을 했을 경우 재귀를 한 위치에서 아래에 있는 곳으로 이동한다.
    if len(ans) == M :
        print(*ans)
        return
    # N만큼 for문을 돌면서 모든 경우의 수를 체크한다.
    for i in range(N) :
        # 이전 들어갔던 수와 현재를 비교를 해서 다른 수와 방문을 하지않았던 곳이면 통과 아니면 건너뛴다.
        if checked != A[i] and not visited[i] :
            ans.append(A[i]) # 정답에 숫자를 넣어준다.
            checked = A[i] # checked 변수에 현재 숫자로 업데이트를 해준다.
            visited[i] = 1 # 방문 표시를 해준다.
            combination()
            # 위에 if문에서 return을 받으면 오는 위치이다.
            # 정답을 출력하고 맨뒤에 있는 숫자만 제거하고, 방문을 0으로 수정한다.
            ans.pop()
            visited[i] = 0


N,M = map(int,input().split()) # 배열의 길이는 N, 출력할 숫자의 개수는 M
A = sorted(list(map(int,input().split()))) # 배열의 숫자를 담아주고 오름차순으로 정렬을 해준다.
# 같은 곳을 두 번 방문하면 안되기 때문에 방문을 했는지 알 수 있는 배열을 N크기 만큼 생성해준다. 
# 예) 1 3 5 7 배열에서 1 1이라는 답은 나올 수 없다.
visited = [0] * N 
ans = list() # 정답을 담을 리스트

combination()