import sys

input = sys.stdin.readline

word = input().rstrip()
obj = list()
ans = list()
for w in word :
    obj.append(ord(w))
    
for _ in range(int(input())) :
    find,s,e = input().split()
    s = int(s)
    e = int(e)
    find = ord(find)
    total = 0
    for i in range(s,e + 1) :
        if find == obj[i] :
            total += 1
    ans.append(str(total))
    
print("\n".join(ans))