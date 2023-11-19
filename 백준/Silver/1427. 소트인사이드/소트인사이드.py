import sys

N = sys.stdin.readline()
arr = []
for nm in N :
  arr.append(nm)
  
print("".join(sorted(arr,reverse=True)))