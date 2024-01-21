import sys

input = sys.stdin.readline

N,M = map(int,input().split())
parking = [int(input()) for _ in range(N)]
cars = [int(input()) for _ in range(M)]
price = 0
current_parking = [0] * N
wait_cars = []
for _ in range(M * 2) :
    in_out = int(input())
    is_parking = False
    if in_out > 0 :
        for i in range(len(current_parking)) :
            if current_parking[i] == 0 :
                current_parking[i] = in_out
                price += cars[in_out - 1] * parking[i]
                is_parking = True
                break
        if not is_parking :
            wait_cars.append(in_out)
    else :
        for i in range(len(current_parking)) :
            if current_parking[i] == -in_out :
                current_parking[i] = 0
                break
        
        if len(wait_cars) > 0 :
            car = wait_cars.pop(0)
            for i in range(len(current_parking)) :
                if current_parking[i] == 0 :
                    current_parking[i] = car
                    price += cars[car - 1] * parking[i]
                    is_parking = True
                    break

print(price)