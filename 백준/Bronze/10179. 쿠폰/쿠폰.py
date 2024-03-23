import sys

input = sys.stdin.readline
N = int(input())

for _ in range(N) :
    T = float(input())
    print("$",end="")
    print("{:.2f}".format(T - (T *0.2)))