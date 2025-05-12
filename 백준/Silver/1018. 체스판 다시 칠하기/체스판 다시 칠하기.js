const readLine = require('fs').readFileSync('dev/stdin').toString().trim();
const [K, ...chessboard] = readLine.split('\n');
const [N, M] = K.split(' ').map((num) => Number(num));

const chess_w = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW'];
const chess_b = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB'];

function checkChessboard(x, y) {
  let result_w = 0;
  let result_b = 0;
  for (let i = 0; i < 8; i++) {
    for (let j = 0; j < 8; j++) {
      if (chessboard[i + x][j + y] != chess_w[i][j]) result_w += 1;
      if (chessboard[i + x][j + y] != chess_b[i][j]) result_b += 1;
    }
  }

  return Math.min(result_w, result_b);
}

let result = Number.MAX_SAFE_INTEGER;

for (let i = 0; i < N - 7; i++) {
  for (let j = 0; j < M - 7; j++) {
    result = Math.min(result, checkChessboard(i, j));
  }
}

console.log(result);
