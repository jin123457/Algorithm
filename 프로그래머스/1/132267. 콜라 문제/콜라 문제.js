function solution(a, b, n) {
  let answer = 0;
  while(n >= a) {
    let rest = n % a;
    n = parseInt(n / a);
    n *= b;
    answer += n;
    n += rest;
  }
  return answer
}