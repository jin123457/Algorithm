function solution(s) {
  let answer = [-1];
  for (let i = 1; i < s.length; i++) {
    let value = s[i];
    let near = -1;
    for (let j = i - 1; j >= 0; j--) {
      if (s[j] == value) {
        near = i - j;
        break;
      }
    }
    answer.push(near);
  }
  return answer;
}