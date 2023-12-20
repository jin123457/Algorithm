N = int(input()) 
A = [int(input()) for _ in range(N)]
left_nm = 0
right_nm = 0
left = 0
right = 0

for i in A :
  if i > left_nm :
    left_nm = i
    left += 1

for j in reversed(A) :
  if j > right_nm :
    right_nm = j
    right += 1

print(left,right,sep="\n")