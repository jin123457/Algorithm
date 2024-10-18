function solution(numbers, hand) {
    let answer = '';
    const keypad = {
        '1' : [0,0],
        '2' : [0,1],
        '3' : [0,2],
        '4' : [1,0],
        '5' : [1,1],
        '6' : [1,2],
        '7' : [2,0],
        '8' : [2,1],
        '9' : [2,2],
        '*' : [3,0],
        '0' : [3,1],
        '#' : [3,2],
    }
    let left_hand = [3,0];
    let right_hand = [3,2];

    for(let number of numbers){
        if(keypad[number][1] == 0){
            answer += 'L';
            left_hand = keypad[number];
        } else if(keypad[number][1] == 2){
            answer += 'R';
            right_hand = keypad[number];
        } else {
            let left = Math.abs(left_hand[0] - keypad[number][0]) + Math.abs(left_hand[1] - keypad[number][1]);
            let right = Math.abs(right_hand[0] - keypad[number][0]) + Math.abs(right_hand[1] - keypad[number][1]);
            if(left > right) {
                answer += 'R';
                right_hand = keypad[number];
            } else if(left < right) {
                answer += 'L';
                left_hand = keypad[number];
            } else if(hand == "right"){
                answer += 'R';
                right_hand = keypad[number];
            } else if(hand == "left"){
                answer += 'L';
                left_hand = keypad[number];
            }
        }
    }
    return answer;
}