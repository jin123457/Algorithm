function solution(progresses, speeds) {
    const answer = [];
    let maxProgress = 0;
    for(let i = 0;i < progresses.length;i++) {
        const current = Math.ceil((100 - progresses[i]) / speeds[i]);
        if(maxProgress < current) {
            maxProgress = current;
            answer.push(0);
        }
        
        if(maxProgress >= current) answer[answer.length - 1] += 1;
    }
    
    return answer;
}