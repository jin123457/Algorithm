import sys

input = sys.stdin.readline

N = input().rstrip()
A = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ans = []
for a in A :
    ans.append(N.count(a))
print(*ans)