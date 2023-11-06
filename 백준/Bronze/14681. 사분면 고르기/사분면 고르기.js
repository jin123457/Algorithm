const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(0).toString().split("\n");

solution(parseInt(input[0]), parseInt(input[1]));

function solution(A, B) {
  if (A > 0 && B > 0) {
    console.log(1);
  } else if (A < 0 && B > 0) {
    console.log(2);
  } else if (A < 0 && B < 0) {
    console.log(3);
  } else if (A > 0 && B < 0) {
    console.log(4);
  }
}
