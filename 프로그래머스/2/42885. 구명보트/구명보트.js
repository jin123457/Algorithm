function solution(people, limit) {
    let answer = 0;
    let index = 0;
    const sortPeople = people.sort((a,b) => b - a);
    let lastIndex = sortPeople.length - 1;
    while (lastIndex >= index) {
        if (sortPeople[index] + sortPeople[lastIndex] <= limit) {
            lastIndex -= 1;
        }
        index += 1;
        answer += 1;
    }

    return answer;
}