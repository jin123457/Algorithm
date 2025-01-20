function solution(absolutes, signs) {
    let answer = 0;
    absolutes.map((num,i) => {
        if(!signs[i]) return answer += -num
        
        answer += num
    });
    
    return answer;
}