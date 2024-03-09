import sys

input = sys.stdin.readline

N = input().rstrip()
ans = []

for n in N :
    
    if n.isupper() :
        ans.append(n.lower())
    else :
        ans.append(n.upper())
print("".join(ans))