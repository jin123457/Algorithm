import sys

input = sys.stdin.readline

N = int(input())
t = ['1','2','3','4','5','6','7','8','9']
st = ['S','L','R','K']
stL = 0
stS = 0
stR = 0
stK = 0
skill = list(input().rstrip())
total = 0
for i in range(len(skill)) :
    if skill[i] in t and stK == 0 and stR == 0 :
        total += 1
    else :
        if skill[i] == "S" : stS += 1

        if skill[i] == "L" : stL += 1

        if skill[i] == "R" :
            if stL > 0 and stK == 0 :
                stL -= 1
                total += 1
                if stR > 1 :
                    stR -= 1
            else :
                stR += 1

        if skill[i] == "K" :
            if stS > 0 and stR == 0 :
                stS -= 1
                total += 1
                if stK > 1 :
                    stK -= 1
            else :
                stK += 1
print(total)