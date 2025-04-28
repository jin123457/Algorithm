const readLine = require('fs').readFileSync('dev/stdin').toString().trim();
const [N, ...input] = readLine.split('\n');
let answer = 0;
for (let i = 0; i < N; i++) {
  const charArr = [];
  let isChar = false;
  for (let j = 0; j < input[i].length; j++) {
    if (input[i][j] === charArr[charArr.length - 1]) {
      continue;
    }

    if (charArr.includes(input[i][j])) {
      isChar = true;
      break;
    }
    charArr.push(input[i][j]);
  }
  if (!isChar) {
    answer++;
  }
}

console.log(answer);
