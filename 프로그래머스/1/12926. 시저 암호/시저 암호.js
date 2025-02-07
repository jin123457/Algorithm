function solution(s, n) {
    let answer = '';
    for(const word of s) {
        let askii = word.charCodeAt();
        
        if(askii == "32") {
            answer += ' ';
        } else {
            askii += n;
            
            if(askii > 90 && word == word.toUpperCase()) {
                askii -= 26;
            } else if(askii > 122 && word == word.toLowerCase()) {
                askii -= 26;
            }
            answer += String.fromCharCode(askii);
        }
    }
    return answer;
}