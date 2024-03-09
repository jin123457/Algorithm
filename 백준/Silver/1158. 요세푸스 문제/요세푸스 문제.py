import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())
sit = deque(i for i in range(1,N + 1))
ans = []
for i in range(len(sit)) :
    sit.rotate(-(K - 1))
    ans.append(str(sit.popleft()))

print("<",end="")
print(", ".join(ans),end="")
print(">")