function solution(array) {
    const sortedArr = array.sort((a,b) => a-b);
    return sortedArr[Math.floor(array.length / 2)];
}