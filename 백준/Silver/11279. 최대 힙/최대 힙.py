import sys
import heapq
input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N) :
    M = int(input())
    if M != 0 :
        heapq.heappush(heap,-M)
    else :
        if len(heap) > 0 :
            print(-heapq.heappop(heap))
        else :
            print(0)