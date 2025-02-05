function solution(s) {
    let answer = s.toLowerCase();
    let newWord = '';
    let wordIndex = 0;
    for(let i = 0;i < answer.length;i++) {
        if(answer[i] == ' ') {
            newWord += ' ';
            wordIndex = 0;
        } else {
            if(wordIndex == 0 || wordIndex % 2 == 0) {
                newWord += answer[i].toUpperCase();
            } else {
                newWord += answer[i];
            }
            
            wordIndex += 1;
        }
    }
    
    return newWord;
}