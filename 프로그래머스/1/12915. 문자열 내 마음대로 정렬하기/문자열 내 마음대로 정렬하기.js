function solution(strings, n) {
    console.log(strings.sort())
    return strings.sort((a,b) => {
        if (a[n] > b[n]) return 1;
        if (a[n] < b[n]) return -1;
        return 0;
    });
}