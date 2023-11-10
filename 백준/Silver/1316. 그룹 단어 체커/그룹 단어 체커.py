N = int(input())
str_arr = [input() for _ in range(N)]
include_str = set()
find_str = []

for string in str_arr :
  before_text = ""
  my_word_status = "TRUE"
  for a in string :
    if a in include_str and before_text != a :
      my_word_status = "False"
    before_text = a
    include_str.add(a)

  if my_word_status == "TRUE" :
    find_str.append(string)
  include_str.clear()
  
print(len(find_str))