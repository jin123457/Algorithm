function solution(targets) {
  let answer = 0;
  let end = 0;

  targets.sort((a, b) => a[1] - b[1]);

  for (let target of targets) {
    let [s, e] = target;

    if (s >= end) {
      answer++;
      end = e;
    }
  }

  return answer;
}