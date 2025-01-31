function solution(s) {
    const answer = [0,0];
    while(s != "1") {
        const zeroCount = s.split('0').length - 1;
        const noZeroCount = s.length - zeroCount;
        answer[0] += 1;
        answer[1] += zeroCount;
        s = noZeroCount.toString(2);
    }
    
    return answer;
}