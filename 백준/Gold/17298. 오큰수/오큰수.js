const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let strdin = fs.readFileSync(filePath).toString().split("\n");

const n = parseInt(strdin[0]);
const input = strdin[1].split(" ").map((item) => parseInt(item));
const stack = [];
const result = [];

for (let i = n - 1; i >= 0; i--) {
  while (stack.length > 0 && stack.at(-1) <= input[i]) {
    stack.pop();
  }
  if (stack.length == 0) {
    result.push(-1);
  } else {
    result.push(stack.at(-1));
  }
  stack.push(input[i]);
}
console.log(result.reverse().join(" "));
