function solution(survey, choices) {
    let survey_list = [
      ["R", "T"],
      ["C", "F"],
      ["J", "M"],
      ["A", "N"],
    ];
    let graph = {
      R: "0,0",
      T: "0,1",
      C: "1,0",
      F: "1,1",
      J: "2,0",
      M: "2,1",
      A: "3,0",
      N: "3,1",
    };
    let survey_result = Array.from(Array(4), () => Array(2).fill(0));

    for (let i = 0; i < survey.length; i++) {
      let [s, e] = survey[i].split("");
      if (choices[i] > 4) {
        let [a, b] = graph[e].split(",");
        survey_result[a][b] += choices[i] - 4;
      } else {
        let [a, b] = graph[s].split(",");
        survey_result[a][b] += 4 - choices[i];
      }
    }
    let answer = "";
    for (let index in survey_result) {
      if (survey_result[index][0] >= survey_result[index][1])
        answer += survey_list[index][0];
      else answer += survey_list[index][1];
    }
    return answer;
}