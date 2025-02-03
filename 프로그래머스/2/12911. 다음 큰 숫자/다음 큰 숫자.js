function solution(n) {
    let answer = n + 1;
    const numberOneCount = n.toString(2).split('1').length - 1;
    let answerOneCount = answer.toString(2).split('1').length - 1;
    while(numberOneCount != answerOneCount) {
        answer += 1;
        
        answerOneCount = answer.toString(2).split('1').length - 1;
    }
    return answer;
}