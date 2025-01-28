function solution(array, commands) {
    const answer = [];
    for(let command of commands) {
        const [i,j,k] = command;
        const findNumber = array.slice(i - 1,j).sort((a,b) => a - b)[k - 1];
        answer.push(findNumber);
    }
    
    return answer;
}