const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

input = input.map((item) => +item);

solution(input[0], input[1]);

function solution(A, B) {
  let stringB = String(B);
  let one = stringB[2];
  let ten = stringB[1];
  let hun = stringB[0];
  console.log(A * one);
  console.log(A * ten);
  console.log(A * hun);
  console.log(A * B);
}
