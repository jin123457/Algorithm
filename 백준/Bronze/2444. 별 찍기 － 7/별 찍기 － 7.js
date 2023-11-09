const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

let number = parseInt(input[0]);

for (let i = 1; i < number; i++) {
  let blank = " ".repeat(number - i);
  let stars = "*".repeat(i + (i - 1));
  console.log(blank + stars);
}
for (let j = number; j > 0; j--) {
  let blank = " ".repeat(number - j);
  let stars = "*".repeat(j + (j - 1));
  console.log(blank + stars);
}
