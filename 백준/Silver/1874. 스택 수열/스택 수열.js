const readLine = require('fs').readFileSync('dev/stdin').toString().trim();
const [N, ...input] = readLine.split('\n');
let pointer = 0;
const stack = [];
const answer = [];
let i = 0;
let isPossible = true;
while (pointer < N) {
  const number = Number(input[pointer]);
  if (stack[stack.length - 1] === number) {
    stack.pop();
    answer.push('-');
    pointer++;
  } else if (stack[stack.length - 1] > number) {
    isPossible = false;

    break;
  } else {
    stack.push(i + 1);
    answer.push('+');
    i++;
  }
}

if (isPossible) {
  console.log(answer.join('\n'));
} else {
  console.log('NO');
}
