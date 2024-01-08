import sys
from collections import deque
input = sys.stdin.readline

def print_copy(K,A) :
    arr = deque()
    is_find = True
    find_time = 1
    for i in range(len(A)) :
        arr.append([i,A[i]])
    
    max_nm = max(A)
    while is_find :
        if arr[0][0] == K and arr[0][1] == max_nm :
            return find_time
        elif arr[0][1] == max_nm :
            find_time += 1
            arr.popleft()
            A.popleft()
            max_nm = max(A)
        else :
            arr.append(arr.popleft())
            A.append(A.popleft())

N = int(input())

for _ in range(N) :
   M,K = map(int,input().split())
   A = deque(map(int,input().split())) 
   print(print_copy(K,A))