const readLine = require('fs').readFileSync('dev/stdin').toString().trim();
const [N, ...peoples] = readLine.split('\n');
const answer = new Array(Number(N)).fill(1);

for (let i = 0; i < peoples.length; i++) {
  for (let j = 0; j < peoples.length; j++) {
    if (i === j) continue;
    const [weightA, heightA] = peoples[i].split(' ').map(Number);
    const [weightB, heightB] = peoples[j].split(' ').map(Number);
    if (weightA < weightB && heightA < heightB) {
      answer[i]++;
    }
  }
}

console.log(answer.join(' '));