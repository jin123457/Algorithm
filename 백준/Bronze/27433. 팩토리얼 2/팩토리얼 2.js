const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const N = fs.readFileSync(filePath).toString().split("\n");

function Factorial(n,answer){
  if(n == 0){
    return answer;
  } else {
    answer *= n;
    n -= 1;
    return Factorial(n,answer)
  }
}
  
console.log(Factorial(N[0],1));