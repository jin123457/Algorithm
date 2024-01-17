import sys

input = sys.stdin.readline

N = int(input())
ans = list()
if N < 10 :
    ori = ['0'] + list(str(N))
    target = ['0'] + list(str(N))
else :
    ori = list(str(N))
    target = list(str(N))
ans.append(ori)

while True :
    T = target
    B = T[-1]
    M = [B] + list(str(sum(list(map(int,T))))[-1])
    NUM = ''
    for m in M :
        NUM += m

    target = list(str(int(NUM[0] + NUM[-1])))
    if ori == M : break
    ans.append(M)
print(len(ans))