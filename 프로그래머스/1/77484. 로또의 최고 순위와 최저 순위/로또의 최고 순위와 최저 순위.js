function solution(lottos, win_nums) {
  const socre = {
    6: 1,
    5: 2,
    4: 3,
    3: 4,
    2: 5,
    1:6,
    0:6,
  }
  let winCount = 0;
  let blind = 0;
  lottos.map((lotto) => {
    if(win_nums.includes(lotto)) winCount += 1;

    if(lotto === 0) blind += 1;
  });

  return [socre[winCount + blind],socre[winCount]];
}