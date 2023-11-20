import sys

N = int(sys.stdin.readline())
obj = {}
for i in range(N) :
  string = input()
  obj[string] = len(string)

key_sort = dict(sorted(obj.items()))
value_sort = sorted(key_sort, key=lambda x : key_sort[x])
print("\n".join(value_sort))