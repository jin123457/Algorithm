import sys

input = sys.stdin.readline

N = int(input())
max_arr = []
max_nm = 0
max_idx = []
arr = []
SH = 0
SW = 0
SM = 0
EH = 0
EW = 0
EM = 0

for _ in range(N) :
    L,H = map(int,input().split())
    arr.append([L,H])

    if max_nm < H :
        max_nm = H
        max_arr = [L]
    elif  max_nm == H :
        max_arr.append(L)

arr = sorted(arr)

for i,v in enumerate(arr) :
    if v[1] == max_nm : max_idx.append(i)

for i in range(max_idx[0] + 1) :
    if SH < arr[i][1] :
        if SH > 0 :
            SM += (SH * (arr[i][0] - SW))

        SW = arr[i][0]
        SH = arr[i][1]

for i in range(len(arr) - 1,max_idx[-1] - 1,-1) :
    if EH < arr[i][1] :
        if EH > 0 :
            EM += (EH * (EW - arr[i][0]))

        EW = arr[i][0]
        EH = arr[i][1]

if len(max_arr) == 1 : 
    print(SM + EM + max_nm)
else :
    max_arr.sort()
    maxW = (max_arr[-1] - max_arr[0]) + 1
    print(SM + EM + (max_nm * maxW))