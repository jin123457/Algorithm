function solution(players, callings) {
    const arr = [];
    const fastPlayer = new Map();
    const latePlayer = new Map();
    players.forEach((el,i) => {
        fastPlayer.set(el,i);
    })
     players.forEach((el,i) => {
        latePlayer.set(i,el);
    })
    for(let call of callings){
        let callPlayerIndex = fastPlayer.get(call);
        let callBeforePlayer = latePlayer.get(callPlayerIndex - 1);
        fastPlayer.set(call, callPlayerIndex - 1);
        fastPlayer.set(callBeforePlayer, callPlayerIndex);
        latePlayer.set(callPlayerIndex, callBeforePlayer);
        latePlayer.set(callPlayerIndex -1, call);
    }
    for (let [key, val] of fastPlayer.entries()) {
        arr[val]  = key;
    }
    return arr;
}