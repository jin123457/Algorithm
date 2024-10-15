function solution(participant, completion) {
  let answer = "";
  let start_people = new Map();
  for (let part of participant) {
    if (!start_people.has(part)) {
      start_people.set(part, 1);
    } else {
      start_people.set(part, start_people.get(part) + 1);
    }
  }

  for (let com of completion) {
    if (start_people.has(com)) {
      if (start_people.get(com) > 1) {
        start_people.set(com, start_people.get(com) - 1);
      } else {
        start_people.delete(com);
      }
    }
  }
  answer = String(...start_people.keys());
  return answer;
}