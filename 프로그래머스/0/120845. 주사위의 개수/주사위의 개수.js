function solution(box, n) {
    const answer = box.reduce((acc,cur) => {
        const newNum = parseInt(cur / n,10);
        return acc *= newNum
    },1);
    return answer;
}