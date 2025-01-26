function solution(numbers) {
    const answer = [];
    for(let i = 0;i < numbers.length;i++) {
        for(let j = i + 1;j < numbers.length;j++) {
            const sumNum = numbers[i] + numbers[j];
            if(!answer.includes(sumNum)) answer.push(sumNum);
        }
    }
    
    return answer.sort((a,b) => a - b);
}