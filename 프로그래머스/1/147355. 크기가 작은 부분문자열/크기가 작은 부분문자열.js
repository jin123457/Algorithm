function solution(t, p) {
  let answer = 0;
  for (let i = 0; i <= t.length - p.length; i++) {
    let comparison = "";
    comparison += t[i];
    for (let j = i + 1; j < i + p.length; j++) {
      comparison += t[j];
    }

    if (parseInt(comparison) <= p) answer += 1;
  }
  return answer;
}