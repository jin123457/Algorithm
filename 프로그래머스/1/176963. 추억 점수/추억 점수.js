function solution(name, yearning, photo) {
    var answer = [];
    const peopleInfo = new Map();
    for(let i = 0;i < name.length;i++){
        peopleInfo.set(name[i],yearning[i]);
    }
    
    for(let i = 0;i < photo.length;i++){
        let yearningTotal = 0;
        let yearningPoint = 0;
        for(let people of photo[i]){
            let yearningPoint = peopleInfo.get(people);
            if(yearningPoint == undefined){
                yearningPoint = 0;
            }
            yearningTotal += yearningPoint;
        }
        answer.push(yearningTotal);
    }
    return answer;
}