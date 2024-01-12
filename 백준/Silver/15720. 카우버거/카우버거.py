import sys

input = sys.stdin.readline

B,C,D = map(int,input().split())
B_arr = sorted(list(map(int,input().split())),reverse=True)
C_arr = sorted(list(map(int,input().split())),reverse=True)
D_arr = sorted(list(map(int,input().split())),reverse=True)
max_nm = max(B,C,D)
total = 0
ori_total = 0
for i in range(max_nm) :
    B,C,D = B - 1,C - 1,D - 1
    
    if B >= 0 :
        ori_total += B_arr[i]
        if C >= 0 and D >= 0 :
            total += int(B_arr[i] * 0.9)
        else :
            total += B_arr[i]
            
    if C >= 0 :
        ori_total += C_arr[i]
        if B >= 0 and D >= 0 :
            total += int(C_arr[i] * 0.9)
        else :
            total += C_arr[i]

    if D >= 0 :
        ori_total += D_arr[i]
        if B >= 0 and C >= 0 :
            total += int(D_arr[i] * 0.9)
        else :
            total += D_arr[i]
print(ori_total,total,sep="\n")