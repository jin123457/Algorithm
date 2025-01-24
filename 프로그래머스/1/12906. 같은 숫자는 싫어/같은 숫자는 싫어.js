function solution(arr) {
    const answer = [];
    arr.map((x,i) => {
        if(x != arr[i - 1]) return answer.push(x);
        return;
    })
    
    return answer;
}