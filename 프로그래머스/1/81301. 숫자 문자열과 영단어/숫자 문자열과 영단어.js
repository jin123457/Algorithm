function solution(s) {
    let answer = '';
    let word = '';
    const numberArr = ['0','1','2','3','4','5','6','7','8','9'];
    const stringArr = {
        'zero' : 0,
        'one' : 1,
        'two' : 2,
        'three' : 3,
        'four' : 4,
        'five' : 5,
        'six' : 6,
        'seven' : 7,
        'eight' : 8,
        'nine' : 9,
    }
    
    for(let x of s) {
        if(!numberArr.includes(x)) {
            word += x;
            
            if(stringArr[word] || stringArr[word] === 0) {
                
                answer += stringArr[word];
                word = '';
            }
        } else {
            if(word !== '') {
                answer += stringArr[word];
                word = '';
            }
            
            answer += x;
        }
    }
    return parseInt(answer);
}