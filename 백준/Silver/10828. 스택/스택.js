const readLine = require('fs').readFileSync('dev/stdin').toString().trim();
const [N, ...input] = readLine.split('\n');
const stack = [];
const answer = [];
for (const x of input) {
  const [command, num] = x.split(' ');

  if (command === 'push') {
    stack.push(num);
  } else if (command === 'pop') {
    if (stack.length === 0) {
      answer.push(-1);
    } else {
      answer.push(stack.pop());
    }
  } else if (command === 'size') {
    answer.push(stack.length);
  } else if (command === 'empty') {
    answer.push(stack.length === 0 ? 1 : 0);
  } else if (command === 'top') {
    answer.push(stack.length === 0 ? -1 : stack[stack.length - 1]);
  }
}
console.log(answer.join('\n'));
