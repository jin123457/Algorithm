const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let [n, ...input] = fs.readFileSync(filePath).toString().split("\n");

let finish = null;
let cureentStart = null;
let cureentFinish = null;
let tmp = 0;
let tmp2 = 0;
const result = [];
input.sort(function (a, b) {
  if (parseInt(a.split(" ")[1]) == parseInt(b.split(" ")[1])) {
    if (parseInt(a.split(" ")[0]) > parseInt(b.split(" ")[0])) {
      return 1;
    }
    if (parseInt(a.split(" ")[0]) < parseInt(b.split(" ")[0])) {
      return -1;
    }
  } else {
    if (parseInt(a.split(" ")[1]) > parseInt(b.split(" ")[1])) {
      return 1;
    }
    if (parseInt(a.split(" ")[1]) < parseInt(b.split(" ")[1])) {
      return -1;
    }
  }
});
for (let i = 0; i < input.length; i++) {
  if (i == 0) {
    finish = input[i].split(" ")[1];
    cureentStart = parseInt(input[i].split(" ")[0]);
    cureentFinish = parseInt(input[i].split(" ")[1]);
    result.push(input[i]);
  } else {
    let startTime = parseInt(input[i].split(" ")[0]);
    let finishTime = parseInt(input[i].split(" ")[1]);
    if (finish <= startTime) {
      if (tmp <= startTime || tmp === 0) {
        tmp = startTime;
        if (tmp2 <= finishTime || tmp2 === 0) {
          if (startTime <= finishTime) {
            result.push(input[i]);
            tmp = startTime;
            tmp2 = finishTime;
            finish = input[i].split(" ")[1];
          }
        }
      }
    }
  }
}

console.log(result.length);
