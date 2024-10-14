function solution(k, score) {
  let answer = [];
  let legend = [];
  score.forEach((v, i) => {
    if (i < k) {
      legend.push(v);
    } else {
      if (legend[0] < v) {
        legend.shift();
        legend.push(v);
      }
    }
    legend.sort((a, b) => a - b);
    answer.push(legend[0]);
  });
  return answer;
}