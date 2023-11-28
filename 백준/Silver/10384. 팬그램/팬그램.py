import sys
from collections import deque
input = sys.stdin.readline

N = int(input()) # 몇 개의 문자열을 검사할건지에 대한 수

# for문을 N만큼 돌면서 검사할 문자열을 가지고 온다.
# 가지고 온 문자열은 소문자로 처리를 해준다.
for i in range(N) :
  pangram_str = deque()
  pangram_str = deque(map(str,input().lower()))
  cnt = 0 # 몇 번 팬그램이 완성됐는지에 대한 수
  # 알파벳 리스트 초기화
  alpabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z']
  j = 1
  # 검사할 문자열을 하나하나 꺼내오면서 알파벳 배열 안에 검사할 문자열이 있을 시 알파벳 리스트에서 삭제해준다.
  # 알파벳 리스트의 길이가 0이 됐을 시 팬그램이 완성된 것이므로, 알파벳 배열을 초기화해주고 cnt 변수에 1를 더해준다.
  while len(pangram_str) > 0 :
    if ord(pangram_str[0]) >= 97 and ord(pangram_str[0]) <= 122 :
      if pangram_str[0] in alpabet:
        alpabet.remove(pangram_str[0])
        pangram_str.popleft()
        if len(alpabet) == 0 :
          alpabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z']
          cnt += 1
          j = 1
      else :
        
        if len(pangram_str) < len(alpabet) : break
        elif len(pangram_str) > j:
          pangram_str.append(pangram_str.popleft())
          j += 1
        else : break
    else :
      pangram_str.popleft()
        
  # cnt의 개수에 따라 출력해준다.
  if cnt == 0 :
    print(f"Case {i + 1}: Not a pangram")
  elif cnt == 1 :
    print(f"Case {i + 1}: Pangram!")
  elif cnt == 2 :
    print(f"Case {i + 1}: Double pangram!!")
  elif cnt == 3 :
    print(f"Case {i + 1}: Triple pangram!!!")