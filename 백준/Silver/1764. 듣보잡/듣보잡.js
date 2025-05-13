const readLine = require('fs').readFileSync('dev/stdin').toString().trim();
const [K, ...input] = readLine.split('\n');
const [N, M] = K.split(' ').map((num) => parseInt(num, 10));
const noHearNames = input.splice(0, N);
const noSeeNames = input;
const noHearSeeNames = new Map();

for (let x of noHearNames) {
  noHearSeeNames.set(x, noHearSeeNames.get(x) ? noHearSeeNames.get(x) + 1 : 0);
}

for (let x of noSeeNames) {
  noHearSeeNames.set(x, noHearSeeNames.get(x) >= 0 ? noHearSeeNames.get(x) + 1 : 0);
}

const newArr = [...noHearSeeNames]
  .map((info) => {
    const [name, val] = info;

    if (val === 1) return name;

    return '';
  })
  .filter((info) => info !== '')
  .sort((a, b) => {
    if (a < b) return -1;
    if (a > b) return 1;
    return 0;
  });

console.log(newArr.length);
console.log(newArr.join('\n'));