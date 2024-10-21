function solution(s) {
    let answer = [];
    let arr = s.split(" ").map(x => parseInt(x,10));
    let min_nm = answer.push(Math.min(...arr));
    let max_nm = answer.push(Math.max(...arr));
    return answer.join(" ");
}