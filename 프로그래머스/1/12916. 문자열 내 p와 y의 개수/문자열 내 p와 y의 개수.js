function solution(s){
    let pCount = 0;
    let yCount = 0;
    s.split('').map((x) => {
        if(x.toLowerCase() == 'p') pCount += 1;
        if(x.toLowerCase() == 'y') yCount += 1;
    })

    return pCount == yCount ? true : false;
}