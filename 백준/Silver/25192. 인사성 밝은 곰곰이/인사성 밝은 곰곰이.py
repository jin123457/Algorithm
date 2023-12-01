import sys
input = sys.stdin.readline
N = int(input())
new_user = False
count = 0
chat_user = set()
for i in range(N) :
    chat = input().rstrip()

    if chat == "ENTER" :
        new_user = True
        if len(chat_user) > 0 :
            chat_user.clear()
    else :
        if new_user and chat not in chat_user :
            chat_user.add(chat)
            count += 1

print(count)