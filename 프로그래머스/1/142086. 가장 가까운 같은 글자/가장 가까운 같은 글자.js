function solution(s) {
  let answer = [-1];
  for (let i = 1; i < s.length; i++) {
    let value = s.slice(0, [i]).split("").reverse().indexOf(s[i]);
    let near = -1;

    if (value > -1) near = value + 1;

    answer.push(near);
  }
  return answer;
}