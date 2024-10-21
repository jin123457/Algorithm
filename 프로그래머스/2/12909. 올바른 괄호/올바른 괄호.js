function solution(s) {
    let answer = true;
    const stack = s.split("").reduce((p,n) => {
        if(n == "(") {
            p.push(n);
        } else {
            if(p.length == 0) {
                answer = false;
            } else {
                p.pop();
            }
        }
        return p
    },[])
    if(stack.length) answer = false;
    return answer;
}