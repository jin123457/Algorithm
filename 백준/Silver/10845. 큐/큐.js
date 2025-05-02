const readLine = require('fs').readFileSync('dev/stdin').toString().trim();
const [N, ...input] = readLine.split('\n');
const queue = [];
const answer = [];
for (const x of input) {
  const [command, number] = x.split(' ');
  if (command === 'push') {
    queue.push(number);
  } else if (command === 'pop') {
    if (queue.length === 0) {
      answer.push(-1);
    } else {
      answer.push(queue.shift());
    }
  } else if (command === 'size') {
    answer.push(queue.length);
  } else if (command === 'empty') {
    answer.push(queue.length === 0 ? 1 : 0);
  } else if (command === 'front') {
    answer.push(queue.length === 0 ? -1 : queue[0]);
  } else if (command === 'back') {
    answer.push(queue.length === 0 ? -1 : queue[queue.length - 1]);
  }
}
console.log(answer.join('\n'));
