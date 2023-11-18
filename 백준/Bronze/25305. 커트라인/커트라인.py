N,K = map(int,input().split()) # 입력받는 자연수의 개수는 N, 상을 받는 인원은 K
arr = list(map(int,input().split())) # 학생들의 성적 점수 리스트
arr.sort() # 학생들의 점수대로 정렬을 한다. 오름차순
arr.reverse() # 학생들의 점수대로 정렬을 한 리스트를 반대로 다시 정렬한다. 내림차순
print(arr[K - 1]) # 상을 받는 학생에서 제일 낮은 점수를 가지고 와서 출력한다.