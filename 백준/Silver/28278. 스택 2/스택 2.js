const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const [N, ...input] = fs.readFileSync(filePath).toString().split("\n");

const stack = [];
const answer = [];
for (const command of input) {
    const act = command.split(" ");
    if (act[0] == "1") {
        stack.push(act[1]);
    } else if (act[0] == "2") {
        if (stack.length > 0) {
            const pop = stack.pop();
            answer.push(pop);
        } else {
            answer.push(-1);
        }
    } else if (act[0] == "3") {
        answer.push(stack.length);
    } else if (act[0] == "4") {
        if (stack.length > 0) {
            answer.push(0);
        } else {
            answer.push(1);
        }
    } else if (act[0] == "5") {
        if (stack.length > 0) {
            answer.push(stack[stack.length - 1]);
        } else {
            answer.push(-1);
        }
    }
}

console.log(answer.join("\n"));