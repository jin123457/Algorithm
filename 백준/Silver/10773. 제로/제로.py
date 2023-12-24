import sys

input = sys.stdin.readline

N = int(input())
ans = list()

for _ in range(N) :
    nm = int(input())

    if not nm :
        ans.pop()
    else :
        ans.append(nm)

print(sum(ans))