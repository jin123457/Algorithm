function solution(n) {
    return parseInt(Number(n).toString(3).split('').reverse().join(''),3);
}