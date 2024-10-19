function solution(X, Y) {
    let answer = [];
    const x_obj = new Map();
    X.split("").map((x) =>  x_obj.set(x, x_obj.has(x) ? x_obj.get(x) + 1 : 1));
    const y_obj = new Map();
    Y.split("").map((y) =>  y_obj.set(y, y_obj.has(y) ? y_obj.get(y) + 1 : 1));
    
    ['9','8','7','6','5','4','3','2','1','0'].map((n) => {
        if(x_obj.has(n) && y_obj.has(n)) {
            let min_nm = Math.min(x_obj.get(n),y_obj.get(n));
            for(let i = 0; i < min_nm;i++) {
                answer.push(n)
            }
        }
    })
    
    if(!answer.length) return "-1";
    else if(answer[0] == "0") return "0";
    else return answer.join("");
}