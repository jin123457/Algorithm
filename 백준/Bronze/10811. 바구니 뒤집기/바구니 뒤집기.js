const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let [[n, m], ...input] = fs
  .readFileSync(filePath)
  .toString()
  .split("\n")
  .map((x) => x.split(" ").map(Number));

let arr = Array(n)
  .fill()
  .map((_, i) => i + 1);
for (let [i, j] of input) {
  let newArr = [];
  for (let idx = i - 1; idx < j; idx++) {
    newArr.push(arr[idx]);
  }
  newArr.reverse();
  arr.splice(i - 1, j - i + 1, ...newArr);
}
console.log(arr.join(" "));
