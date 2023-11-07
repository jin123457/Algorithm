function solution(name, yearning, photo) {
    // 정답을 담는 Array
    var answer = [];
    // 사람들의 정보, 그리움 점수를 담는 Object 생성
    const peopleInfo = new Map();
    // 사람들의 정보는 key 값, 그리움 점수는 value 값으로 넣기
    for(let i = 0;i < name.length;i++){
        peopleInfo.set(name[i],yearning[i]);
    }
    // photo Array는 이차원 배열이여서 하나씩 꺼내기
    for(let i = 0;i < photo.length;i++){
        // 총 점수 초기화
        let yearningTotal = 0;
        // 각 배열에 대한 점수 초기화
        let yearningPoint = 0;
        // 배열 마다 사람들의 이름 꺼내오기
        for(let people of photo[i]){
            // 꺼내온 사람의 이름을 위에서 생성한 peopleInfo 라는 Object에서 검색
            let yearningPoint = peopleInfo.get(people);
            // 검색한 후 사람의 정보가 없을 때는 0점 처리
            if(yearningPoint == undefined){
                yearningPoint = 0;
            }
            // 검색한 사람이 있을 경우 해당되는 사람의 그리움 점수를 추가해주기
            yearningTotal += yearningPoint;
        }
        // 하나에 배열이 끝날 때 총점수를 answer Array에 넣어주기
        answer.push(yearningTotal);
    }
    
    return answer;
}
