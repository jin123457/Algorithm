function solution(answers) {
    const answerCount = [0, 0, 0];
    const answer = [];
    const one = [1, 2, 3, 4, 5] // 5
    const two = [2, 1, 2, 3, 2, 4, 2, 5] // 8
    const three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] // 10
    
    answers.map((x,i) => {
        if(x == one[i % one.length]) answerCount[0] += 1;
        if(x == two[i % two.length]) answerCount[1] += 1;
        if(x == three[i % three.length]) answerCount[2] += 1;
    });
    
    for(let i = 0;i < answerCount.length;i++) {
        if(answerCount[i] == Math.max(...answerCount)) answer.push(i + 1);
    }
    
    return answer;
}