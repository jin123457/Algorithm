const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split(" ");

solution(parseInt(input[0]), parseInt(input[1]), parseInt(input[2]));

function solution(A, B, C) {
  if (A == B && B == C) {
    console.log(10000 + A * 1000);
  } else if (A == B || B == C || C == A) {
    if (A == B || A == C) {
      console.log(1000 + A * 100);
    } else {
      console.log(1000 + B * 100);
    }
  } else {
    console.log(Math.max(A, B, C) * 100);
  }
}
