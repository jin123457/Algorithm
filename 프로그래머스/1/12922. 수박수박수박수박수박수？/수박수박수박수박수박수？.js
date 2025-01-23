function solution(n) {
    var answer = '';
    if(n % 2 === 0) {
      return "수박".repeat(Math.floor(n/2));
    }
    return "수박".repeat(Math.floor(n/2))+"수";
}