import sys

input = sys.stdin.readline

N = int(input())
A = list(list(map(str,input().rstrip())) for _ in range(N))
heart = list()
head_x = 0
head_y = 0
leftArm = 0
rightArm = 0
waist = 0
left_leg = 0
right_leg = 0
for i in range(len(A)) :
    for j in range(len(A[i])) :
        if len(heart) == 0 and A[i][j] == "*" :
            heart.append((i + 2,j + 1))
            head_x = i
            head_y = j
        elif head_x + 1 == i :
            if head_y > j  and A[i][j] == "*" :
                leftArm += 1
            elif  head_y < j  and A[i][j] == "*" :
                rightArm += 1
        elif head_x + 2 <= i :
            if head_y == j  and A[i][j] == "*" :
                waist += 1
            if head_y > j  and A[i][j] == "*" :
                left_leg += 1
            if head_y < j  and A[i][j] == "*" :
                right_leg += 1


print(*heart[0])
print(leftArm,rightArm,waist,left_leg,right_leg)