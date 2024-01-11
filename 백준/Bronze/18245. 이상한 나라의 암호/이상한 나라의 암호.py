import sys

input = sys.stdin.readline
i = 0

while True :
    N = input().rstrip()
    i += 1
    skip = 0
    if N == "Was it a cat I saw?" : break
    ans = []
    for j in range(len(N)) :
        if j != 0 :
            if skip == i :
                skip = 0
                ans.append(N[j])
            else :
                skip += 1
        else :
            ans.append(N[j])
    
    print("".join(ans))