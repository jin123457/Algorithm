function solution(numbers) {
    const maxNumbers = numbers.sort((a,b) => b - a);
    return maxNumbers[0] * maxNumbers[1];
}