import sys
input = sys.stdin.readline
# dequeue로 문제풀기
N = int(input())

def decode_word(arr) :
    ans = []
    for _ in range(len(arr)-1,-1,-1) :
        for words in arr :
            if words :
                word = words.pop()
                ans.append(word)

    return ans
for _ in range(N) :
    queue = []
    password = input().rstrip()
    word_avg = int(len(password) ** 0.5) 
    for i in range(0,len(password),word_avg) :
        words = list(map(str,password[i:i+word_avg]))
        queue.append(words)
    print("".join(decode_word(queue)))