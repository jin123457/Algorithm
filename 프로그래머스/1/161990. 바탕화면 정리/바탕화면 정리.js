function solution(wallpaper) {
  let answer = [];
  let min_row = Number.MAX_SAFE_INTEGER;
  let min_col = Number.MAX_SAFE_INTEGER;
  let max_row = 0;
  let max_col = 0;

  wallpaper.forEach((wall, i) => {
    wall.split("").forEach((w, j) => {
      if (w == "#") {
        min_row = Math.min(min_row, i);
        max_row = Math.max(max_row, i);
        min_col = Math.min(min_col, j);
        max_col = Math.max(max_col, j);
      }
    });
  });

  answer = [min_row, min_col, max_row + 1, max_col + 1];
  return answer;
}