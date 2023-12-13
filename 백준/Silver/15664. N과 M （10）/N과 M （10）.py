import sys

input = sys.stdin.readline

def combination() :
    global idx
    checked = 0
    
    if len(ans) == M : 
        print(*ans)
        return

    for i in range(N) :
        if checked < A[i] and not visited[i] :
            if len(ans) > 0 and ans[idx-1] > A[i] : continue
            ans.append(A[i])
            checked = A[i]
            visited[i] = 1
            idx += 1
            combination()
            ans.pop()
            visited[i] = 0
            idx -= 1
            

N,M = map(int,input().split())
A = sorted(list(map(int,input().split())))
visited = [0] * N
ans = list()
idx = 0
combination()