const readLine = require('fs').readFileSync('dev/stdin').toString().trim();
let N = Number(readLine);

let count = 0;
while (N >= 5) {
  N = Math.floor(N / 5);
  count += N;
}
console.log(count);
