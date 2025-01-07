function solution(n) {
    return String(n).split('').reduce((acc,cur) => acc + parseInt(cur,10),0);
}