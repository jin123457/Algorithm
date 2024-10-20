function solution(num) {
    var answer = 0;
    let time = 0;
    while(num > 1) {
        if(num % 2 == 0 ){
            num /= 2;
        } else {
            num *= 3;
            num += 1;
        }
        
        if(time >= 500) {
            answer = -1;
            break;
        }
        time++;
        if(num == 1) answer = time;
    }
    return answer;
}