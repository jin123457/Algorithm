function solution(park, routes) {
  let is_find_start = false;
  let answer = [0, 0];
  for (let i = 0; i < park.length; i++) {
    for (let j = 0; j < park[i].length; j++) {
      if (park[i][j] == "S") {
        answer = [i, j];
        is_find_start = true;
        break;
      }
    }
    if (is_find_start) break;
  }

  function moveCheck(park, dir, cnt) {
    let is_break = false;
    let over_cnt = cnt;
    if (dir == "W" || dir == "E") {
      over_cnt *= dir == "W" ? -1 : 1;
      let next_move = answer[1] + over_cnt;
      if (0 > next_move || next_move >= park[0].length) {
        is_break = true;
      }
    } else {
      over_cnt *= dir == "N" ? -1 : 1;
      let next_move = answer[0] + over_cnt;
      if (0 > next_move || next_move >= park.length) {
        is_break = true;
      }
    }

    if (!is_break) {
      if (dir == "S" || dir == "E") {
        let b = dir == "S" ? answer[0] : answer[1];
        for (let i = b + 1; i <= b + cnt; i++) {
          let d = dir == "S" ? park[i][answer[1]] : park[answer[0]][i];
          if (d == "X") {
            is_break = true;
            break;
          }
        }
      } else {
        let b = dir == "N" ? answer[0] : answer[1];
        for (let i = b; i >= b - cnt; i--) {
          let d = dir == "N" ? park[i][answer[1]] : park[answer[0]][i];
          if (d == "X") {
            is_break = true;
            break;
          }
        }
      }
    }
    return is_break;
  }

  for (let move of routes) {
    let [dir, cnt] = move.split(" ");

    cnt = parseInt(cnt);
    if (moveCheck(park, dir, cnt)) continue;
    if (dir == "E") {
      answer[1] += cnt;
    } else if (dir == "S") {
      answer[0] += cnt;
    } else if (dir == "W") {
      answer[1] -= cnt;
    } else if (dir == "N") {
      answer[0] -= cnt;
    }
  }
  return answer;
}