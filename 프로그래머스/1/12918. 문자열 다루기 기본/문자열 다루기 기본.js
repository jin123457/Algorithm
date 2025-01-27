function solution(s) {
    let answer = true;
    const numbers = [0,1,2,3,4,5,6,7,8,9];
    for(let x of s) {
        if(!numbers.includes(Number(x))) answer = false
    }
    return (s.length == 4 || s.length == 6) ? answer : false;
}