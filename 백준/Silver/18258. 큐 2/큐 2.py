import sys
from collections import deque
input = sys.stdin.readline
# dequeue로 문제풀기
N = int(input())
queue = deque()
ans = []
for i in range(N) :
    j = input().split()
    if j[0] == 'push' :
        queue.append(j[1])
    elif j[0] == 'pop' :
        if len(queue) > 0 :
            top = queue.popleft() # pop(0) 대신에 popleft()를 써준다.
            ans.append(top)
        else :
            ans.append('-1')
    elif j[0] == 'size' :
        ans.append(str(len(queue)))
    elif j[0] == 'empty' :
        if len(queue) == 0 :
            ans.append('1')
        else :
            ans.append('0')
    elif j[0] == "front" :
        if len(queue) > 0 :
            ans.append(queue[0])
        else :
            ans.append('-1')
    else :
        if len(queue) > 0 :
            ans.append(queue[-1])
        else :
            ans.append('-1')
            
print("\n".join(ans))