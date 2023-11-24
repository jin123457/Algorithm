import sys
from collections import deque

input = sys.stdin.readline

# dequeue로 문제풀기
# dequeue는 앞과 뒤에서 값을 빼고 넣을 수 있다.
# appendleft, popleft 기억해 둘 것!!
N = int(input())
dequeue = deque()
ans = []
for i in range(N) :
    j = input().split()
    if j[0] == '1' :
        dequeue.appendleft(j[1])
    elif j[0] == '2' :
         dequeue.append(j[1])
    elif j[0] == '3' :
        if len(dequeue) > 0 :
            top = dequeue.popleft()
            ans.append(top)
        else :
            ans.append('-1')
    elif j[0] == '4' :
        if len(dequeue) > 0 :
            top = dequeue.pop()
            ans.append(top)
        else :
            ans.append('-1')
    elif j[0] == '5' :
        ans.append(str(len(dequeue)))
    elif j[0] == '6' :
        if len(dequeue) == 0 :
            ans.append('1')
        else :
            ans.append('0')
    elif j[0] == "7" :
        if len(dequeue) > 0 :
            ans.append(dequeue[0])
        else :
            ans.append('-1')
    else :
        if len(dequeue) > 0 :
            ans.append(dequeue[-1])
        else :
            ans.append('-1')

print("\n".join(ans))