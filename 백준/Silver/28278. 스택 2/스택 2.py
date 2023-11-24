import sys

N = int(sys.stdin.readline())
stack = []
ans = []
for i in range(N) :
    j = sys.stdin.readline().split()
    
    if j[0] == '1' :
        stack.append(j[1])
    elif j[0] == '2' :
        if len(stack) > 0 :
            top = stack.pop()
            ans.append(top)
        else :
            ans.append('-1')
    elif j[0] == '3' :
        ans.append(str(len(stack)))
    elif j[0] == '4' :
        if len(stack) == 0 :
            ans.append('1')
        else :
            ans.append('0')
    else :
        if len(stack) > 0 :
            ans.append(stack[-1])
        else :
            ans.append('-1')
print("\n".join(ans))