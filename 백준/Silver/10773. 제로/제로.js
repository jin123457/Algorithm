const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const [N, ...input] = fs
    .readFileSync(filePath)
    .toString()
    .split("\n");

const stack = [];

for (let i = 0; i < N; i++) {
    const number = Number(input[i]);
    if (!number) {
        stack.pop();
    } else {
        stack.push(number);
    }
}
const sum = stack.reduce((acc, cur) => acc + cur, 0);
console.log(sum);
