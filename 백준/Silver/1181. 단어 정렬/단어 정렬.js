const readLine = require('fs').readFileSync('dev/stdin').toString().trim();
const [N, ...input] = readLine.split('\n');

const noDuplicate = [...new Set(input)];

const sortArr = noDuplicate.sort((a, b) => {
  if (a.length > b.length) return 1;
  else if (a.length < b.length) return -1;
  else return a.localeCompare(b);
});
console.log(sortArr.join('\n'));
