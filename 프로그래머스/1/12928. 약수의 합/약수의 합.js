function solution(n) {
  let number = 1;
  const divisors = [];

  while(number <= n) {
    if(n % number === 0) divisors.push(number);

    number++;
  }
  
  return divisors.length ? divisors.reduce((acc,cur) => acc + cur) : 0;
}