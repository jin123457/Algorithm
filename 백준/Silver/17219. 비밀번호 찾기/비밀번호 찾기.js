const readLine = require('fs').readFileSync('dev/stdin').toString().trim();
const [N, ...input] = readLine.split('\n');
const [K, M] = N.split(' ').map((num) => Number(num));
const map = new Map();
const answer = [];

for (const x of input.splice(0, K)) {
  const [siteUrl, password] = x.split(' ');

  map.set(siteUrl, password);
}

for (const siteUrl of input) {
  answer.push(map.get(siteUrl));
}

console.log(answer.join('\n'));