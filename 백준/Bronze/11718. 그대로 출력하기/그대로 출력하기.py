import sys
c = sys.stdin.readlines()
for string in c :
  string = string[0:int(len(string)) -1]
  print(string)