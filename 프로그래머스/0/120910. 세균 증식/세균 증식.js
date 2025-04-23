function solution(n, t) {
    var answer = n;
    Array.from({length : t},() => {
        answer *= 2;
    })
    return answer;
}