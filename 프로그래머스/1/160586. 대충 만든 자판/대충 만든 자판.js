function solution(keymap, targets) {
  let answer = Array.from(Array(targets.length).fill(0));
  let max_len = 0;
  keymap.map((x) => (max_len = Math.max(max_len, x.length)));
  for (let j = 0; j < targets.length; j++) {
    let sum_index = 0;
    let succes_word = true;
    for (let w of targets[j]) {
      let min_index = 0;
      let is_find = false;
      for (let i = 0; i < max_len; i++) {
        for (let key of keymap) {
          if (key[i] == w) {
            min_index += i + 1;
            is_find = true;
            break;
          }
        }
        if (is_find) break;
      }
      if (!min_index) succes_word = false;
      sum_index += min_index;
    }
    if (!succes_word) answer[j] = -1;
    else answer[j] = sum_index;
  }

  return answer;
}