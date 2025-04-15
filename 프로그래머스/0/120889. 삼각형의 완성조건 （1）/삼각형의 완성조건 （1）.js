function solution(sides) {
    const sortSides = sides.sort();
    return sortSides[2] >= sortSides[0] + sortSides[1] ? 2 : 1;
}