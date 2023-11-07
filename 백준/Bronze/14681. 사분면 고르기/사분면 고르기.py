# 1쿼터 양수,양수 2쿼터 음수,양수 3쿼터 음수,음수 4쿼터 양수,음수

A,B = int(input()),int(input())

if A > 0 and B > 0 :
    print('1')
elif A < 0 and B > 0 :
    print('2')
elif A < 0 and B < 0 :
    print('3')
elif A > 0 and B < 0 :
    print('4')