student_nm = [int(input()) for _ in range(28)]
all_student_nm = [n for n in range(1,31,1)]

def check_student(nm) :
  del all_student_nm[all_student_nm.index(nm)]

for student in student_nm :
  check_student(student)

print(min(all_student_nm))
print(max(all_student_nm))