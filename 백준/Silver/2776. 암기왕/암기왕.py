import sys

input = sys.stdin.readline

T = int(input())
ans = list()
for _ in range(T) :
    N = int(input())
    NN = set(map(int,input().split()))
    M = int(input())
    MM = list(map(int,input().split()))

    for m in MM :
        if m in NN :
            ans.append('1')
        else :
            ans.append('0')

print("\n".join(ans))