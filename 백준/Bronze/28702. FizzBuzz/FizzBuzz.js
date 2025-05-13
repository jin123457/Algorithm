const readLine = require('fs').readFileSync('dev/stdin').toString().trim();
const [...input] = readLine.split('\n');

function FizzBuzz(num) {
  if (num % 3 === 0 && num % 5 === 0) {
    return 'FizzBuzz';
  }

  if (num % 3 === 0) {
    return 'Fizz';
  }

  if (num % 5 === 0) {
    return 'Buzz';
  }

  return num;
}
let lastNumber = 0;
const filterNaN = input.filter((num) => {
  if (!isNaN(num)) lastNumber = Number(num);
  else lastNumber += 1;
});

console.log(FizzBuzz(lastNumber + 1));
