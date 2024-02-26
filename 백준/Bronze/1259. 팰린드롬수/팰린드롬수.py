import sys

input = sys.stdin.readline

while True :
    nm = input().rstrip()
    if nm == '0' :break
    arr = list(nm)
    reverse_arr = list(reversed(list(nm)))
    if reverse_arr[0] == "0" :
        reverse_arr.pop(0)
    if int("".join(arr)) == int("".join(reverse_arr)) :
        print('yes')
    else :
        print('no')