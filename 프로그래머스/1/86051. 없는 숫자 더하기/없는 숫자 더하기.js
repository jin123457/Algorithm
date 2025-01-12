function solution(numbers) {
    return [0,1,2,3,4,5,6,7,8,9].filter((x) => !numbers.includes(x)).reduce((acc,cur) => acc + cur,0);
}