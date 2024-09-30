function solution(diffs, times, limit) {
    
    let diff_arr = diffs.map((x) => parseInt(x));
    let time_arr = times.map((x) => parseInt(x));
    const LIMIT = parseInt(limit);

    let [left, right] = [
      Math.min(diffs.reduce((acc, cur) => Math.min(acc, cur), 1)),
      Math.max(diffs.reduce((acc, cur) => Math.max(acc, cur), 1)),
    ];
    let mid = parseInt((left + right) / 2);

    while (left < right) {
      let play_time = 0;
      for (let i = 0; i < diffs.length; i++) {
        if (mid >= diffs[i]) {
          play_time += times[i];
        } else {
          let fail = diffs[i] - mid;
          play_time += (times[i - 1] + times[i]) * fail + times[i];
        }
      }

      if (play_time > LIMIT) {
        left = mid + 1;
      } else {
        right = mid;
      }

      mid = parseInt((left + right) / 2);
    }
    return mid;
}