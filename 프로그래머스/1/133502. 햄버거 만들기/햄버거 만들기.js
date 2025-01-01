function solution(ingredient) {
  let answer = 0;
  const arr = [];
  let i = 0;
  while(ingredient.length >= i) {
    if(arr.length === 0 && ingredient[i] === 1 && ingredient[i + 1] === 2) {
      arr.push(i);
      i += 1;
    } else if(arr.length === 1 && ingredient[i] === 2) {
      arr.push(i);
      i += 1;
    } else if(arr.length === 2 && ingredient[i] === 3) {
      arr.push(i);
      i += 1;
    } else if(arr.length === 3 && ingredient[i] === 1) {
      arr.push(i);
      i += 1;
    } else if(arr.length === 4) {
      i = arr[0] - 4;
      ingredient.splice(arr[0],4);
      arr.length = 0;
      answer += 1;
    } else {
      arr.length = 0;
      if(arr.length === 0 && ingredient[i] === 1 && ingredient[i + 1] === 2) {
        arr.push(i);
      }
      i += 1;
    }
  };

  return answer;
}