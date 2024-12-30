function solution(k, m, score) {
    let answer = 0;
    let lastPoint = m - 1;
    const greateApples = score.sort((a,b) => b - a);

    while(greateApples.length - 1 >= lastPoint) {
        answer += greateApples[lastPoint] * m;
        lastPoint += m;
    }

    return answer;
}