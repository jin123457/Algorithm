function solution(board, moves) {
    let answer = 0;
    let doll_box = [];
    let Machine = new Array(board[0].length + 1).fill().map(_ => []);
    for(let n of board) {
        n.forEach((v,i) => {
            if(v > 0)Machine[i + 1].push(v)
        });
    }

    for(let move of moves){
        if(Machine[move].length){
            let get_doll = Machine[move].shift();
            doll_box.push(get_doll);
            if(doll_box.length > 1){
                if(get_doll == doll_box[doll_box.length - 2]){
                    doll_box.pop();
                    doll_box.pop();
                    answer += 2;
                }
            }
        }
    }


    return answer;
}