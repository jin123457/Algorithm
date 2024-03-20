import sys

input = sys.stdin.readline

N = int(input())

C = B = G = 0
arr = input().rstrip().split()
for i in range(len(arr)) :

    if arr[i] == '1' :
        C += 1
    elif arr[i] == '-1' :
        B += 1
    else :
        G += 1

if len(arr) % 2 == 0:
    mid = len(arr) // 2
else :
    mid = len(arr) // 2 + 1
    
if mid <= G :
    print('INVALID')
else :
    if C > B :
        print('APPROVED')
    else :
        print('REJECTED')