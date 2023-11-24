import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

for i in range(N) :
    queue = deque()
    student_arr = list(map(int,input().split()))
    del student_arr[0]
    for score in sorted(student_arr,reverse=True) :
        queue.append(score)
    gap = 0
    
    for key,score in enumerate(queue) :
        if key < len(queue) - 1 :
            gap = max(gap,(queue[key] - queue[key + 1]))

    print(f"Class {i + 1}")
    print(f"Max {max(queue)}, Min {min(queue)}, Largest gap {gap}")