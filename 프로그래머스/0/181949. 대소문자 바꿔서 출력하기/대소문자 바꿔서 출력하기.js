const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    let str = '';
    for(let x of input[0]) {
        if(x === x.toUpperCase()) str += x.toLowerCase();
        if(x === x.toLowerCase()) str += x.toUpperCase();
    }
    console.log(str)
});