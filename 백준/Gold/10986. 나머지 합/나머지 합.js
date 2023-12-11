const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

const A = input.shift().split(" ").map(Number);
const N = A[0];
const M = A[1];
const arr = input.shift().split(" ").map(Number);
arr.unshift(0);
const copyArr = Array.from({ length: N }, () => 0);
let result = 0;
let map = new Map();

for (i in arr) {
  if (i == 0) copyArr[i] += arr[i];
  else copyArr[i] = (arr[i] + copyArr[i - 1]) % M;
}

for (let i = 1; i < copyArr.length; i++) {
  map.has(copyArr[i])
    ? map.set(copyArr[i], map.get(copyArr[i]) + 1)
    : map.set(copyArr[i], 1);
  if (copyArr[i] == 0) {
    result += 1;
  }
}

function combination(n, r) {
  let res = 1;
  for (let i = 0; i < r; i++) {
    res *= (n - i) / (i + 1);
  }
  return res;
}

for (let x of map.keys()) {
  result += combination(map.get(x), 2);
}

console.log(result);
