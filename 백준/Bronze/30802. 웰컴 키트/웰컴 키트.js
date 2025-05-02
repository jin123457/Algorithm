const readLine = require('fs').readFileSync('dev/stdin').toString().trim();
const [N, ...input] = readLine.split('\n');
const shirtSize = input[0].split(' ').map((x) => Number(x));
const [T, P] = input[1].split(' ').map((x) => Number(x));
const maxShirtSize = Math.max(...shirtSize);
let shirtAnswer = 0;
for (const s of shirtSize) {
  shirtAnswer += Math.ceil(s / T);
}
const penAnswer = [Math.floor(N / P), N - P * Math.floor(N / P)];

console.log(shirtAnswer);
console.log(penAnswer.join(' '));