const readLine = require('fs').readFileSync('dev/stdin').toString().trim();
const [M, ...input] = readLine.split("\n");
const [N, T] = M.split(" ").map((num) => Number(num));
const busInfo = input.map((num) => num.split(" ").map((num1) => Number(num1))); // 시작 시간, 간격, 대수

const answer = [];
for (let i = 0; i < N; i++) {
  let startTime = busInfo[i][0];
  const busWaitTime = busInfo[i][1];
  const busCount = busInfo[i][2];

  for (let j = 0; j < busCount; j++) {
    if (startTime >= T) {
      answer.push(startTime);
      break;
    }

    startTime += busWaitTime;
  }
}

if (answer.length === 0) {
  console.log(-1);
} else {
  const minBusTime = Math.min(...answer);
  console.log(minBusTime - T);
}