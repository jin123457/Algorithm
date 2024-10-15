function solution(n, lost, reserve) {
  let student = new Array(n + 1).fill(1);
  lost.map((l) => (student[l] = 0));
  reserve.map((r) => (student[r] += 1));

  for (let i = 0; i < student.length; i++) {
    if (student[i] == 2) {
      if (student[i - 1] == 0) {
        student[i - 1] += 1;
      } else if (student[i + 1] == 0) {
        student[i + 1] += 1;
      }
      student[i] -= 1;
    }
  }
  return student.reduce((p, n) => p + n, -1);
}