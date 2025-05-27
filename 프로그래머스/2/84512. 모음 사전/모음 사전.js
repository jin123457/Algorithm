function solution(word) {
    const alphabet = ['A', 'E', 'I', 'O', 'U'];
    const answer = Array.from({ length: 5 }, () => '');
    let i = 0;
    let j = 0;
    let idx = 0;
    let answerIdx = 0;
    function solutionWord(i) {
      idx++;
      if (i > 4) return;
      for (let j = 0; j < 5; j++) {
        answer[i] = alphabet[j];
        if (answer.slice(0, i + 1).join('') === word) answerIdx = idx;
        solutionWord(i + 1);
      }
    }

    solutionWord(i);
    return answerIdx;
}