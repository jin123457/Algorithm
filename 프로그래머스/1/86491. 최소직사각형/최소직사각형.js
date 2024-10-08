function solution(sizes) {
  let answer = 0;
  let max_row = 0;
  let max_col = 0;
  for (let size of sizes) {
    let [r, c] = size;
    let max_size = Math.max(r, c);
    if (max_size == r) {
      max_row = Math.max(max_row, r);
      max_col = Math.max(max_col, c);
    } else {
      max_row = Math.max(max_row, c);
      max_col = Math.max(max_col, r);
    }
  }
  answer = max_row * max_col;
  return answer;
}