import sys

input = sys.stdin.readline

N = [i for i in range(1,10001)]

for i in range(1,10001) :
    T = list(str(i))
    ori = i
    if i < 10 :
        ori += int(T[-1])
    else :
        for j in list(str(i)) :
           ori += int(j)
    
    if ori in N :
        N.remove(ori)
print(*N,sep="\n")