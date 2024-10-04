function solution(id_list, report, k) {
    let recive_mail = id_list.reduce((info, name) => {
  info[name] = 0;
  return info;
}, {});
let reported_id = id_list.reduce((info, name) => {
  info[name] = [];
  return info;
}, {});

for (let x of report) {
  let [A, B] = x.split(" ");
  if (!reported_id[B].includes(A)) {
    reported_id[B].push(A);
  }
}

for (let x of Object.keys(reported_id)) {
  if (reported_id[x].length >= k) {
    for (let c of reported_id[x]) {
      recive_mail[c] += 1;
    }
  }
}
    return Object.values(recive_mail);
}