import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    N = int(input())
    vote = [int(input()) for _ in range(N)]
    max_vote = max(vote)
    sum_vote = sum(vote)
    cnt_vote = vote.count(max_vote)
    result = sum_vote - max_vote
    
    if max_vote * N == sum_vote or cnt_vote > 1 :
        print("no winner")
    else :
        if max_vote > result :
            print(f"majority winner {vote.index(max_vote) + 1}")
        else :
            print(f"minority winner {vote.index(max_vote) + 1}")