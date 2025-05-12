const readLine = require('fs').readFileSync('dev/stdin').toString().trim();
const [N, ...input] = readLine.split('\n');

const sortArr = input.sort((a, b) => {
  const [x1, y1] = a.split(' ').map((num) => Number(num));
  const [x2, y2] = b.split(' ').map((num) => Number(num));

  if (y1 === y2) {
    return x1 - x2;
  }

  return y1 - y2;
});

console.log(sortArr.join('\n'));
