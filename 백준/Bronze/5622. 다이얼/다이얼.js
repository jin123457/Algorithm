const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

//String.fromCodePoint 97 ~ 122 알파벳
let word = input[0];
let alpalbet = 97;
let total = 0;
for (let i = 0; i <= 9; i++) {
  if (i == 0 || i == 1) {
    continue;
  }
  const tmp = [];

  if (i == 9 || i == 7) {
    tmp.push(String.fromCodePoint(alpalbet).toUpperCase());
    tmp.push(String.fromCodePoint(alpalbet + 1).toUpperCase());
    tmp.push(String.fromCodePoint(alpalbet + 2).toUpperCase());
    tmp.push(String.fromCodePoint(alpalbet + 3).toUpperCase());
    alpalbet += 4;
  } else {
    tmp.push(String.fromCodePoint(alpalbet).toUpperCase());
    tmp.push(String.fromCodePoint(alpalbet + 1).toUpperCase());
    tmp.push(String.fromCodePoint(alpalbet + 2).toUpperCase());
    alpalbet += 3;
  }

  for (let idx = 0; idx < word.length; idx++) {
    if (tmp.includes(word[idx])) {
      total += i + 1;
    }
  }
}
console.log(total);
