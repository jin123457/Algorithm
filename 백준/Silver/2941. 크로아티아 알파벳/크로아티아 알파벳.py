croatia_alpabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']

croatia_str = input()

for i in croatia_alpabet :
  croatia_str = croatia_str.replace(i,'Q')

print(len(croatia_str))