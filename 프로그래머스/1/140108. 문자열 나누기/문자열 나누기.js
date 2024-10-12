function solution(s) {
  let answer = 0;
  let start_word = "";
  let same_cnt = 0;
  let wrong_cnt = 0;
  for (let i = 0; i < s.length; i++) {
    if (start_word == "") {
      start_word = s[i];
      same_cnt = 1;
    } else {
      if (start_word == s[i]) same_cnt += 1;
      else wrong_cnt += 1;
    }

    if (same_cnt == wrong_cnt) {
      same_cnt = 0;
      wrong_cnt = 0;
      start_word = "";
      answer += 1;
    } else if (s.length - 1 == i && (wrong_cnt > 0 || same_cnt > 0)) {
      answer += 1;
    }
  }

  return answer;
}