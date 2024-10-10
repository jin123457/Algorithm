let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const N = input[0];
input.shift();

let arr = input.map((x) => x.split(" "));
let answer = 0;
for (let i = 123; i <= 987; i++) {
  let is_find = true;
  let my_num = String(i);
  if (
    my_num[0] == my_num[1] ||
    my_num[0] == my_num[2] ||
    my_num[1] == my_num[2] || +my_num[0] == 0 ||
    +my_num[1] == 0 ||
    +my_num[2] == 0
  )
    continue;
  for (let x of arr) {
    let [num, s, b] = x;
    let strike = 0;
    let ball = 0;
    if (num[0] == my_num[0]) strike += 1;
    if (num[1] == my_num[1]) strike += 1;
    if (num[2] == my_num[2]) strike += 1;

    if (my_num[0] == num[1] || my_num[0] == num[2]) ball += 1;
    if (my_num[1] == num[0] || my_num[1] == num[2]) ball += 1;
    if (my_num[2] == num[0] || my_num[2] == num[1]) ball += 1;

    if (+s != strike || +b != ball) is_find = false;
  }
  if (is_find) answer += 1;
}

console.log(answer);