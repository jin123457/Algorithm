import sys

input = sys.stdin.readline

A = list(map(int,input().split()))
ASC_A = sorted(A)
DESC_A = sorted(A,reverse=True)

if A == ASC_A : print('ascending')
elif A == DESC_A : print('descending')
else : print('mixed')