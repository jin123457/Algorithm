const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const [n, ...input] = fs.readFileSync(filePath).toString().split("\n");

let people_set = new Set();
people_set.add('ChongChong');

for(let i = 0;i < n;i++){
    const [n,m] = input[i].split(" ");
    if(people_set.has(n) || people_set.has(m)) {
        people_set.add(n)
        people_set.add(m)
    }
}
console.log(people_set.size)