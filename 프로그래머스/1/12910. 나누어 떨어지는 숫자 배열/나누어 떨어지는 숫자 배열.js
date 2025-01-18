function solution(arr, divisor) {
    const answer = [];
    arr.map((x) => {
        if(x % divisor === 0) answer.push(x)
    })
    console.log()
    return answer.length > 0 ? answer.sort((a,b) => a - b) : [-1];
}