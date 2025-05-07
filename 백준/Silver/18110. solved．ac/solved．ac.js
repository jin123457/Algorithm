const readLine = require('fs').readFileSync('dev/stdin').toString().trim();
const [N, ...input] = readLine.split('\n');

if (N === '0') {
  console.log(0);
  return
}

const sortedLevels = input.map((x) => Number(x)).sort((a, b) => a - b);
const minusIndex = Math.round((N / 100) * 15);
const filteredLevels = sortedLevels.slice(minusIndex, N - minusIndex);

const average = filteredLevels.reduce((acc, cur) => acc + cur, 0) / filteredLevels.length;
console.log(Math.round(average));
