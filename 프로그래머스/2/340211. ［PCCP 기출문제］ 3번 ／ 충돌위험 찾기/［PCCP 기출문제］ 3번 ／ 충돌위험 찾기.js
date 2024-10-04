function solution(points, routes) {
    
    let robots_current_point = [];
    let robots_move_points = [];
    let robots = routes.map((a) => {
      let robot_route = a;
      robots_current_point.push(points[robot_route[0] - 1].slice());
      let path = [];
      for (let j = 0; j < robot_route.length - 1; j++) {
        path.push(points[robot_route[j + 1] - 1].slice());
      }
      robots_move_points.push(path);
      return routes.length;
    });

    let answer = 0;
    while (true) {
      let map = {};
      robots_current_point.forEach((x) => (map[x] ? map[x]++ : (map[x] = 1)));
      let cnt = 0;
      map[[-1, -1]] = 0;
      for (const i of Object.values(map)) {
        if (i > 1) {
          cnt++;
        }
      }
      answer += cnt;

      let isMove = false;
      for (let i = 0; i < robots.length; i++) {
        if (robots_move_points[i].length == 0) {
          robots_current_point[i][0] = -1;
          robots_current_point[i][1] = -1;
          continue;
        }
        let move = [
          robots_move_points[i][0][0] - robots_current_point[i][0],
          robots_move_points[i][0][1] - robots_current_point[i][1],
        ];

        if (move[0] != 0) {
          isMove = true;
          const d = move[0] > 0 ? 1 : -1;
          robots_current_point[i][0] += d;
          move[0] -= d;
        } else if (move[1] != 0) {
          isMove = true;
          const d = move[1] > 0 ? 1 : -1;
          robots_current_point[i][1] += d;
          move[1] -= d;
        }

        if (move[0] == 0 && move[1] == 0) {
          // 목표한 곳에 왔을 때 움직이는 배열에서 제일 앞에 좌표를 삭제해준다.
          robots_move_points[i].shift();
        }
      }
      if (isMove == false) break;
    }
    return answer;
}