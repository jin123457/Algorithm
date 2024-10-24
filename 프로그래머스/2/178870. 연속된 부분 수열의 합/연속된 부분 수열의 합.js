function solution(sequence, k) {
  let answer = [];
  let s = 0;
  let e = 0;
  let index_len = sequence.length;
  let save_nm = sequence[0];
  while (sequence.length > s) {
    if (isNaN(save_nm)) break;

    if (k > save_nm) {
      e += 1;
      save_nm += sequence[e];
    } else if (k < save_nm) {
      save_nm -= sequence[s];
      s += 1;
    }
    if (k == save_nm) {
      if (index_len > e - s) {
        index_len = e - s;
        answer = [s, e];
        if (!index_len) break;
      }
      save_nm -= sequence[s];
      s += 1;
    }
  }
  return answer;
}