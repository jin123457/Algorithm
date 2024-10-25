function solution(n) {
    let answer = [];
    answer.push(0);
    answer.push(1);

    for(let i = 2; i <= n;i++) {
        answer.push((answer[i - 2] + answer[i - 1]) % 1234567);
    }

    return answer[answer.length - 1];
}