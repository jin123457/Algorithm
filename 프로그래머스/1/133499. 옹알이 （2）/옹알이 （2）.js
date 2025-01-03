function solution(babbling) {
  let answer = 0;
  const words = ['aya', 'ye', 'woo', 'ma'];
  for(let say of babbling) {
    for(let word of words) {
      if(say.includes(word.repeat(2))) continue;

      say = say.replaceAll(word,' ');
    }

    if(say.replaceAll(' ','') === '') answer += 1;
  }

  return answer;
}