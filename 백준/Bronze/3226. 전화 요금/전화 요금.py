import sys

input = sys.stdin.readline

def time_calculation(time,c_time) :
    global total_money

    hour,min = map(int,time.split(':'))
    for _ in range(1,c_time+1) :
        min += 1

        if hour >= 7 and hour <= 18 :
            total_money += 10
        else : 
            total_money += 5

        if min >= 60 :
            min = 0
            hour += 1
        
        if hour == 24 :
            hour = 0

N = int(input())
total_money = 0

for _ in range(N) :
    time,c_time = input().split()
    time_calculation(time,int(c_time))

print(total_money)