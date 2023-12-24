import sys

input = sys.stdin.readline

N,M = map(int,input().split())
A = dict()
ans = list()

for i in range(M) :
    student = input().rstrip()

    A[student] = i

for i in sorted(A,key=A.__getitem__) : 
    if len(ans) == N : break

    ans.append(i)

print("\n".join(ans))