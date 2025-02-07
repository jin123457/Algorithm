function solution(n, m) {
    const answer = [0,0];
    
    for(let i = 1;i <= Math.min(n,m);i++) {
        if(n % i === 0 && m % i === 0) answer[0] = i;
    }
    
    for(let i = 1;i <= n * m;i++) {
        if(i % n === 0 && i % m === 0) {
            answer[1] = i;
            break;
        }
    }
    
    return answer;
}