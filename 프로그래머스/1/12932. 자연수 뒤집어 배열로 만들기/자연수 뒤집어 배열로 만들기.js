function solution(n) {
    return String(n).split('').reverse().map((x) => parseInt(x));
}