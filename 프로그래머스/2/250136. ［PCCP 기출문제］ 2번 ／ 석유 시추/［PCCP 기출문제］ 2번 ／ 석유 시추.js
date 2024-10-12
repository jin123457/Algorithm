function solution(land) {
  let answer = 0;
  let row = land.length; // 맵의 세로 길이
  let col = land[0].length; // 맵의 가로 길이

  let visied_map = Array.from(Array(row), (_) => Array(col).fill(0));
  let oilIdx = 1;
  let oil_map = new Map();
  let direciton = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];

  function bfs(path) {
    let [r, c] = path;
    let oil_amount = 1;
    let oil_queue = [[r, c]];

    while (oil_queue.length > 0) {
      let [oil_r, oil_c] = oil_queue.shift();
      visied_map[oil_r][oil_c] = oilIdx;

      for (let [dy, dx] of direciton) {
        let y = oil_r + dy;
        let x = oil_c + dx;
        if (
          y >= row ||
          y < 0 ||
          x >= col ||
          x < 0 ||
          visied_map[y][x] != 0 ||
          land[y][x] == 0
        )
          continue;
        oil_amount++;
        visied_map[y][x] = oilIdx;
        oil_queue.push([y, x]);
      }
    }
    oil_map[oilIdx] = oil_amount;
    oilIdx++;
  }

  for (let i = 0; i < row; i++) {
    // land 세로 만큼
    for (let j = 0; j < col; j++) {
      // land 가로 만큼
      if (visied_map[i][j] == 0 && land[i][j]) {
        bfs([i, j]);
      }
    }
  }

  for (let i = 0; i < col; i++) {
    let max_oil = 0;
    let set = new Set();
    for (let j = 0; j < row; j++) {
      if (visied_map[j][i] && !set.has(visied_map[j][i]))
        set.add(visied_map[j][i]);
    }

    set.forEach((oil_idx) => {
      max_oil += oil_map[oil_idx];
    });
    answer = Math.max(answer, max_oil);
  }
  return answer;
}