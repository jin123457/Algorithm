const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim();

const croatiaAlpabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="];

const handleChandeAlpabet = (input) => {
    for (let alpabet of croatiaAlpabet) {
        input = input.split(`${alpabet}`).join("*");
    }
    return input.length;
};

console.log(handleChandeAlpabet(input));

