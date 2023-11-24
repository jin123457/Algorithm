import sys

# deque 없이 문제풀기
N = int(sys.stdin.readline())
que = []
ans = []
cnt = 0
# 큐에서 팝을 쓰려면 시간초과가 나서 index를 하나씩 추가 해줬다.
# 삭제를 안하다보니, 리스트에 길이를 알아하는 구간에서는 cnt 값을 빼줘야한다.
for i in range(N) :
    j = sys.stdin.readline().split()
    if j[0] == 'push' :
        que.append(j[1])
    elif j[0] == 'pop' :
        if len(que) - cnt > 0 :
            top = que[cnt]
            ans.append(top)
            cnt += 1
        else :
            ans.append('-1')
    elif j[0] == 'size' :
        ans.append(str(len(que) - cnt))
    elif j[0] == 'empty' :
        if len(que) - cnt == 0 :
            ans.append('1')
        else :
            ans.append('0')
    elif j[0] == "front" :
        if len(que) - cnt > 0 :
            ans.append(que[cnt])
        else :
            ans.append('-1')
    else :
        if len(que) - cnt > 0 :
            ans.append(que[-1])
        else :
            ans.append('-1')
print("\n".join(ans))