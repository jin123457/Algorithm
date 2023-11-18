import sys
input = sys.stdin.readline
N = int(input()) # 자연수 몇 개를 입력받을 것인지 입력받는 자연수
arr = [int(input()) for _ in range(N)]
arr.sort()

for nm in arr :
    print(nm)
