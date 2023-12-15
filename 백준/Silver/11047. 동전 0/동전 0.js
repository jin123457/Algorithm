const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let [n, ...input] = fs.readFileSync(filePath).toString().split("\n");

const moneyList = input.reverse();
let myMoney = parseInt(n.split(" ")[1]);
let moneyCnt = 0;

for (let i = 0; i < moneyList.length; i++) {
  if (myMoney >= parseInt(moneyList[i])) {
    let moneyCount = Math.floor(myMoney / parseInt(moneyList[i]));
    moneyCnt += Math.floor(myMoney / parseInt(moneyList[i]));
    myMoney -= parseInt(moneyList[i]) * moneyCount;
  }
}

console.log(moneyCnt);
