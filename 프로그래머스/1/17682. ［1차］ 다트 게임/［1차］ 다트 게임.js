function solution(dartResult) {
  const arr = [];
  for(let i = 0;i < dartResult.length;i++) {
    if(dartResult[i] === 'S' || dartResult[i] === 'D' || dartResult[i] === 'T') {
      let score = 0;
      if(dartResult[i] === 'S') score = 1;
      if(dartResult[i] === 'D') score = 2;
      if(dartResult[i] === 'T') score = 3;
      if(dartResult[i - 1] === '0' && dartResult[i - 2] === '1') {
        arr.push(10 ** score);
      } else {
        arr.push(parseInt(dartResult[i - 1],10) ** score);
      }
    }

    if(dartResult[i] === '*') {
      arr[arr.length - 1] *= 2;
      if(arr.length > 1) {
        arr[arr.length - 2] *= 2;
      }
    }

    if(dartResult[i] === '#') {
      arr[arr.length - 1] *= -1;
    }
  }
  const answer = arr.reduce((acc,cur) => acc + cur,0);

  return answer;
}