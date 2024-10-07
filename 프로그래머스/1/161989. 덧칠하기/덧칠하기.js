function solution(n, m, section) {
  let answer = 0;
  let wall = Array.from(Array(n + 1).fill(1));
  section.map((x) => (wall[x] = 0));
  let paint_finish = false;

  while (!paint_finish) {
    if (!section.length) {
      paint_finish = true;
      break;
    }

    let current_paint = section.shift();
    wall[current_paint] = 1;
    answer += 1;
    for (let i = current_paint + 1; i < current_paint + m; i++) {
      if (wall[i] == 0) {
        wall[i] = 1;
        section.shift();
      }
    }
  }
  return answer;
}