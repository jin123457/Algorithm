import sys

input = sys.stdin.readline
N = int(input())
meet_chongchong = False
dance = set()
count = 0
for _ in range(N) :
    M,K = input().split()

    if K == "ChongChong" or M == "ChongChong" :
        meet_chongchong = True
        dance.add(K)
        dance.add(M)
        continue

    if meet_chongchong and (M in dance or K in dance) :
        dance.add(K)
        dance.add(M)

print(len(dance))