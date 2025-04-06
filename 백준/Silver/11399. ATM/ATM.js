const readLine = require('fs').readFileSync('dev/stdin').toString().trim();
const [N, times] = readLine.split('\n');
const convertTimes = times
    .split(' ')
    .map(Number)
    .sort((a, b) => a - b);
let waitTime = 0;
const minTime = convertTimes.reduce((acc, cur) => {
    acc += cur + waitTime;
    waitTime += cur;
    return acc;
}, 0);
console.log(minTime);