all_info_arr = [list(map(str,input().split())) for _ in range(20)]
score_info = {
  'A+' : '4.5',
  'A0' : '4.0',
  'B+' : '3.5',
  'B0' : '3.0',
  'C+' : '2.5',
  'C0' : '2.0',
  'D+' : '1.5',
  'D0' : '1.0',
  'F' : '0.0'
}
score_arr = []
subject_score_arr = []

for info in all_info_arr :
  if info[2] == "P" : continue
    
  score_arr.append(float(info[1]) * float(score_info[info[2]]))
  subject_score_arr.append(float(info[1]))
  
print(round(sum(score_arr) / sum(subject_score_arr),6))