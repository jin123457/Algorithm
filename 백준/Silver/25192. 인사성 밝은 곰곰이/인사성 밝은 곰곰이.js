const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const [n, ...input] = fs.readFileSync(filePath).toString().split("\n");

let answer = 0;
let people_set = new Set();

for(let i = 0;i < n;i++){
    if(input[i] == 'ENTER') {
        answer += people_set.size;
        people_set.clear();
    } else if(!people_set.has(input[i])){
        people_set.add(input[i]);
    }
}
console.log(answer + people_set.size)