import sys

input = sys.stdin.readline

N = int(input())
obj = {}
ans = []
for _ in range(N) :
    info = list(map(int,input().split()))
    obj[info[0]] = info[1:]



for i in range(4) :
    high_grade = 0
    high_grade_student = 0
    for student in sorted(obj.items(),key=lambda x:x[0],reverse=True) :
        if student[0] not in ans :
            high_grade = max(high_grade,student[1][i])
            if student[1][i] == high_grade :
                high_grade_student = student[0]

    ans.append(high_grade_student)
    
print(*ans)