const readLine = require('fs').readFileSync('dev/stdin').toString().trim();

let N = readLine.split('\n');
let answer = 0;
let find = true;

while (N > 0) {
  if (N - 3 >= 0 && N % 5 !== 0) {
    N -= 3;
    answer += 1;
  } else if (N % 5 === 0) {
    N -= 5;
    answer += 1;
  } else if (N < 3) {
    find = false;
    break;
  }
}

if (!find) {
  console.log(-1);
} else {
  console.log(answer);
}
