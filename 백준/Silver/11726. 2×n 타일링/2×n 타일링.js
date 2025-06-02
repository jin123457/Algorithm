const readLine = require('fs').readFileSync('dev/stdin').toString().trim();
const N = Number(readLine);

const answer = [0, 1, 2];

for (let i = 3; i <= N; i++) {
  answer.push((answer[i - 1] + answer[i - 2]) % 10007);
}

console.log(answer[N]);
