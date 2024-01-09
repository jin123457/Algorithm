import sys

input = sys.stdin.readline

def prime_check(A,mn) :
    for i in range(4,len(A) + 1,2) :
        A.remove(i)
    for i in range(3,len(A) + 1,2) :
        for j in range(i * 2,mn,i) :
            if j in A :
                A.remove(j)

T = int(input())
A = [int(input()) for _ in range(T)]
nm_arr = [i for i in range(2,max(A) + 1)]
prime_check(nm_arr,max(A))

for find_nm in A :
    is_find = False
    for nm1 in nm_arr :
        for nm2 in nm_arr :
            for nm3 in nm_arr :
                if nm1 + nm2 + nm3 == find_nm :
                    print(nm1,nm2,nm3)
                    is_find = True
                    break
            if is_find : break
        if is_find : break
    
    if not is_find :
        print(0)