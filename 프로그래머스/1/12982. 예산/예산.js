function solution(d, budget) {
    let answer = 0;
    let total = 0;
    d.sort((a,b) => a - b).map((money) => {
        if(total + money <= budget) {
            answer += 1;
            total += money;
        }
    })
    return answer;
}