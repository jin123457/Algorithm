function solution(a, b) {
    let answer = 0;
    let minNm = Math.min(a,b);
    let maxnm = Math.max(a,b);
    for(let i = minNm;i <= maxnm;i++) {
        answer += i;
    }
    return answer;
}