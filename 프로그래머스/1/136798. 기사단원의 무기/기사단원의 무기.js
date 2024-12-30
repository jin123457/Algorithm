function solution(number, limit, power) {
  let answer = 0;
  
  for(let i = 1;i <= number;i++) {
    let count = 0;
    for (let j = 1;j * j <= i;j++) {
      if (i % j === 0) {
        count += 1;
        if (j * j < i) {
          count += 1;
        }
      }
    }

    if (count > limit) {
      answer += power;
    } else {
      answer += count;
    }
  }
  return answer;
}