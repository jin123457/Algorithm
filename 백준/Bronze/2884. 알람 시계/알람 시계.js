const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split(" ");

solution(parseInt(input[0]), parseInt(input[1]));

function solution(hour, min) {
  if (min - 45 < 0) {
    let minusMin = 60 - 45 + min;
    let minusHour = 0;
    if (hour > 0) {
      minusHour = hour - 1;
    } else {
      minusHour = 24 - 1;
    }
    console.log(`${minusHour} ${minusMin}`);
  } else {
    let minusMin = min - 45;
    console.log(`${hour} ${minusMin}`);
  }
}
