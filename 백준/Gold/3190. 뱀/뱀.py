import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
snake = deque()
snakeHead = [0,0]
time = 0
dire = 0
for _ in range(K) :
    AR,AC = map(int,input().split())
    board[AR - 1][AC - 1] = 1

MT = int(input())
M = [input().rstrip().split() for _ in range(MT)]
is_dump = False

while True :
    
    
    if dire == 0 :
        snakeHead[1] += 1

        if 0 > snakeHead[1] or snakeHead[1] >= N or snakeHead in snake :
            is_dump = True
            break

        if board[snakeHead[0]][snakeHead[1]] == 1 :
            snake.append([snakeHead[0],snakeHead[1] - 1])
            board[snakeHead[0]][snakeHead[1]] = 0
        elif len(snake) :
            snake.popleft()
            snake.append([snakeHead[0],snakeHead[1] - 1])

    if dire == 1 :
        snakeHead[0] += 1

        if 0 > snakeHead[0] or snakeHead[0] >= N or snakeHead in snake :
            is_dump = True
            break

        if board[snakeHead[0]][snakeHead[1]] == 1 :
            snake.append([snakeHead[0] - 1,snakeHead[1]])
            board[snakeHead[0]][snakeHead[1]] = 0
        elif len(snake) :
            snake.popleft()
            snake.append([snakeHead[0] - 1,snakeHead[1]])

    if dire == 2 :
        snakeHead[1] -= 1


        if 0 > snakeHead[1] or snakeHead[1] >= N or snakeHead in snake :
            is_dump = True
            break

        if board[snakeHead[0]][snakeHead[1]] == 1 :
            snake.append([snakeHead[0],snakeHead[1] + 1])
            board[snakeHead[0]][snakeHead[1]] = 0
        elif len(snake) :
            snake.popleft()
            snake.append([snakeHead[0],snakeHead[1] + 1])

    if dire == 3 :
        snakeHead[0] -= 1

        if 0 > snakeHead[0] or snakeHead[0] >= N or snakeHead in snake :
            is_dump = True
            break

        if board[snakeHead[0]][snakeHead[1]] == 1 :
            snake.append([snakeHead[0] + 1,snakeHead[1]])
            board[snakeHead[0]][snakeHead[1]] = 0
        elif len(snake) :
            snake.popleft()
            snake.append([snakeHead[0] + 1,snakeHead[1]])

    time += 1
    for m in M :
        if int(m[0]) > time : break
        elif int(m[0]) == time  :
            if m[1] == 'D' :
                dire += 1
            else :
                dire -= 1
            dire %= 4
print(time + 1)