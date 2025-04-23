const readLine = require('fs').readFileSync('dev/stdin').toString().trim();
const [N, ...input] = readLine.split('\n');

const answer = input.sort((a, b) => {
  const [x1, y1] = a.split(' ').map(Number);
  const [x2, y2] = b.split(' ').map(Number);

  if (x1 === x2) {
    return y1 - y2;
  }
  return x1 - x2;
});

console.log(answer.join('\n'));