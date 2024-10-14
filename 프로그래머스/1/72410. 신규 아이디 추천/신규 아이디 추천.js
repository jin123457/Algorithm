function solution(new_id) {
  let answer = "";
  for (let word of new_id.toLowerCase()) {
    if (
      word.charCodeAt() == 45 ||
      word.charCodeAt() == 46 ||
      word.charCodeAt() == 95 ||
      (97 <= word.charCodeAt() && word.charCodeAt() <= 122) ||
      (48 <= word.charCodeAt() && word.charCodeAt() <= 57)
    ) {
      answer += word;
    }
  }
  answer = answer.replace(/\.{2,}/g, ".");
  if (answer[0] == ".") answer = answer.slice(1, answer.length);
  if (answer[answer.length - 1] == ".") answer = answer.slice(0, answer.length - 1);
  if (answer.length == 0) answer = "a";
  if (answer.length >= 16) answer = answer.slice(0, 15);
  if (answer[answer.length - 1] == ".")
    answer = answer.slice(0, answer.length - 1);

  if (answer.length <= 2) {
    for (let i = answer.length; i < 3; i++) {
      answer += answer[answer.length - 1];
    }
  }
  return answer;
}