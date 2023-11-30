T = int(input())
ans = []

for _ in range(T) :
    N = list(input())
    cnt = 0
    no_vps = False
    for VPS in N :
        if cnt < 0 : 
            no_vps = True
            break
        if VPS == "(" :
            cnt += 1
        else :
            cnt -= 1
                
    if cnt != 0 or no_vps :
        ans.append('NO')
    else :
        ans.append('YES')

print("\n".join(ans))