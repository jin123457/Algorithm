function solution(arr) {
    const minNum = Math.min(...arr);
    const newArr = arr.filter((num) => num !== minNum);
    return newArr.length ? newArr : [-1];
}