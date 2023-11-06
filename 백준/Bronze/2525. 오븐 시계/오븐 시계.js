const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

let clock = input[0].split(" ");
let timer = input[1];

solution(parseInt(clock[0]), parseInt(clock[1]), parseInt(timer));

function solution(clockHour, clockMin, timer) {
  let plusClockMin = clockMin + timer;
  let restMin = 0;
  if (plusClockMin >= 60) {
    clockHour += parseInt(plusClockMin / 60);
  }

  if (plusClockMin >= 60) {
    restMin = plusClockMin % 60;
  } else {
    restMin = plusClockMin;
  }

  if (restMin == 60) {
    restMin = 0;
  }

  if (clockHour == 24) {
    clockHour = 0;
  } else if (clockHour > 24) {
    clockHour = parseInt(clockHour % 24);
  }
  console.log(`${clockHour} ${restMin}`);
}
