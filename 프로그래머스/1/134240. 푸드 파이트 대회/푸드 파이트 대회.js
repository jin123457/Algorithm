function solution(food) {
    let answer = '';
    food.map((x,i) => {
        if (i != 0) {
            answer += String(i).repeat(Math.floor(x / 2));
        }
    });
    return answer + '0' + answer.split('').reverse().join('');
}