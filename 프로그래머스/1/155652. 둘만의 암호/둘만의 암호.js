function solution(s, skip, index) {
  let answer = "";
  let alpabet = "abcdefghijklmnopqrstuvwxyz";
  for (let word of s) {
    let decode = "";
    let jump_time = 0;
    let start = 0;
    let i = 1;
    while (true) {
      if (alpabet[i] == word && !start) {
        start = 1;
        i == 25 ? (i %= 25) : i++;
        continue;
      }

      if (start) {
        if (!skip.includes(alpabet[i])) {
          jump_time += 1;
        }

        if (jump_time == index) {
          decode = alpabet[i];
          break;
        }
      }
      i == 25 ? (i %= 25) : i++;
    }
    answer += decode;
  }
  return answer;
}