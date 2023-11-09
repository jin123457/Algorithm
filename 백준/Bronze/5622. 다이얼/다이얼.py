N = input()
askii_start = 97
askii_arr = []
chars = ""
j = 1


for i in range(26) :
  
  if i == 18  and j == 4:
    chars += chr(askii_start + i).upper()
    askii_arr.append(list(chars))
    chars = ""
    j = 1
  elif i == 25  and j == 4:
    chars += chr(askii_start + i).upper()
    askii_arr.append(list(chars))
    chars = ""
    j = 1
  elif i != 0 and j == 4:
    askii_arr.append(list(chars))
    chars = ""
    j = 1

  if  i != 18 and i != 25 :
    chars += chr(askii_start + i).upper()
    j += 1

total_time = 0

for alpabet in N :
  find_status = "false"
  total_time += 2
  for askii in askii_arr :
    if find_status == "false" :
      total_time += 1
    askii = "".join(askii)
    if askii.find(alpabet) != -1 :
      find_status = "true"
      

print(total_time)