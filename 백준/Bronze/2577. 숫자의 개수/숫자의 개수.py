import sys

N = str(int(input()) * int(input()) * int(input()))

for i in range(10) :
    print(list(N).count(str(i)))