function isPrime(num) {
    if(num === 2) return true;
    
    for(let i = 2;i <= Math.floor(Math.sqrt(num));i++) {
        if(num % i === 0) return false
    }
    
    return true;
}

function solution(nums) {
    let answer = 0;
    const sumArr = [];
    for(let i = 0;i < nums.length;i++) {
        for(let j = i + 1; j < nums.length;j++) {
            for(let k = j + 1;k < nums.length;k++) {
                const sum = nums[i] + nums[j] + nums[k];
                if(isPrime(sum)) {
                    answer += 1;
                }
            }
        }
    }
    
    return answer;
}