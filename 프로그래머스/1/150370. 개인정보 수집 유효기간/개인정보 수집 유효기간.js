function solution(today, terms, privacies) {
    let [convert_year, convert_month, convert_day] = today
  .split(".")
  .map((x) => parseInt(x));
if (convert_month < 10) {
  convert_month = `0${convert_month}`;
}
if (convert_day < 10) {
  convert_day = `0${convert_day}`;
}
const CONVERT_DATE = `${convert_year}${convert_month}${convert_day}`;
let term_info = {};
for (let i = 0; i < terms.length; i++) {
  let [kind, month] = terms[i].split(" ");
  term_info[kind] = parseInt(month);
}

const PRIVACIES_INFO = privacies.map((x) => x.split(" "));
let end_date_arr = [];

for (let i = 0; i < privacies.length; i++) {
  let [start_date, kind] = PRIVACIES_INFO[i];
  let [year, month, day] = start_date.split(".").map((x) => parseInt(x));
  let update_year = year;
  if (term_info[kind] >= 12) {
    update_year += parseInt(term_info[kind] / 12);
  }
  let update_month = month + parseInt(term_info[kind] % 12);
  let update_day = day - 1;
  if (update_month > 12) {
    update_year += 1;
    update_month -= 12;
  }
  if (update_day < 1) {
    update_month -= 1;
    update_day = 28;
  }

  if (update_month < 10) {
    update_month = `0${update_month}`;
  }
  if (update_day < 10) {
    update_day = `0${update_day}`;
  }
  let update_date = `${update_year}${update_month}${update_day}`;
  if (update_date < CONVERT_DATE) end_date_arr.push(i + 1);
}
    return end_date_arr;
}