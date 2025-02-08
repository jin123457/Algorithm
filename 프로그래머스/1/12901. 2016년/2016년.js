function solution(a, b) {
    const months = [31,29,31,30,31,30,31,31,30,31,30,31];
    const daily = ['SUN','MON','TUE','WED','THU','FRI','SAT'];
    let today = 4;
    const days = (months.slice(0,a - 1).reduce((acc,cur) => acc + cur,0) + b) % 7;
    
    return daily[(today + days) % 7];
}