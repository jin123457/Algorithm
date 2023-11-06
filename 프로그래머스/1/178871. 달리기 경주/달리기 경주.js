function solution(players, callings) {
    // 정답을 담는 Array
    const arr = [];
    // 선수들의 정보를 담는 object
    const playerInfo = new Map();
    // 선수들의 index를 담는 object
    const playerIndex = new Map();
    
    // 선수들의 정보를 key 값으로 index는 value값으로 넣기
    players.forEach((el,i) => {
        playerInfo.set(el,i);
    })
    // 선수들의 index는 key 값으로 정보는 value값으로 넣기
    players.forEach((el,i) => {
        playerIndex.set(i,el);
    })
    
    // 호출되는 array를 value만 꺼내오기
    for(let call of callings){
        // 호출된 선수의 인덱스를 가지고 오기
        let callPlayerIndex = playerInfo.get(call);
        // 호출된 전 선수의 정보를 가지고 오기
        let beforeCallPlayer = playerIndex.get(callPlayerIndex - 1);
        
        // 선수정보를 수정한다.
        
        // 호출된 선수의 인덱스는 - 1 시켜주기
        playerInfo.set(call, callPlayerIndex - 1);
        // 호출된 선수 앞에 있던 선수는 인덱스는 + 1 시켜주기
        playerInfo.set(beforeCallPlayer, callPlayerIndex);
        
        // 선수의 인덱스 부분도 수정을 해준다.
        
        // 호출된 선수 앞에 있던 선수의 인덱스를 + 1 해주기
        playerIndex.set(callPlayerIndex, beforeCallPlayer);
        // 호출된 선수의 인덱스를 -  해주기
        playerIndex.set(callPlayerIndex -1, call);
    }
    
    // 선수 정보를 가지고 있는 Object를 하나씩 풀기
    for (let [key, val] of playerInfo.entries()) {
        // 답을 넣는 Array에 value는 인덱스 값으로, key 값은 value 값으로 넣어준다.
        arr[val]  = key;
    }
    return arr;
}
