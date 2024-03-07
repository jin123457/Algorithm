import sys

input = sys.stdin.readline

def BS(NN,s,e,m) :
    is_find = False
    while s < e :
        mid = (s + e) // 2
        
        if NN[mid] > m : 
            e = mid
        elif NN[mid] < m :
            s = mid + 1
        elif NN[mid] == m :
            is_find  = True
            break

    if is_find :
        return '1'
    else :
        return '0'


T = int(input())
ans = list()

for _ in range(T) :
    N = int(input())
    NN = list(map(int,input().split()))
    M = int(input())
    MM = list(map(int,input().split()))
    
    NN = sorted(NN)
    for m in MM :
        ans.append(BS(NN,0,N,m))

print("\n".join(ans))