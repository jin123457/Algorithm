function solution(array, height) {
    return array.reduce((acc,cur) => {
        if(cur > height) acc +=1;
        return acc;
    },0);
}