function solution(N, stages) {
  const answer = [];
  const obj = []
  for(let i = 1; i <= N;i++){
    let before = stages.length;
    stages = stages.filter((x) => x !== i);
    const fail = before - stages.length;
    obj.push({index : i, fail : fail / before});
  }

  obj.sort((a,b) => b.fail - a.fail).map(x=>answer.push(x.index));

  return answer;
}