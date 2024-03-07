const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let [n, k] = fs.readFileSync(filePath).toString().trim().split("\n");
n = parseInt(n);
k = parseInt(k);

const BS = (start, end) => {
  while (start < end) {
    let mid = Math.floor((start + end) / 2);
    let sum = 0;
    for (let i = 1; i <= n; i++) {
      sum += Math.min(n, Math.floor(mid / i));
    }

    if (k > sum) start = mid + 1;
    else end = mid;
  }

  return end;
};

console.log(BS(1, k));
