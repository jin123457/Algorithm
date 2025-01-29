function solution(n, arr1, arr2) {
    const maps = Array.from({length : n},() => new Array(n).fill(' '));
    arr1.map((num,i) => {
        const changeStr = num.toString(2).padStart(n,0);
        changeStr.split('').map((m,j) => {
            if(maps[i][j] === ' ' && m == 1) maps[i][j] = '#';
        })
    })
    arr2.map((num,i) => {
        const changeStr = num.toString(2).padStart(n,0);
        changeStr.split('').map((m,j) => {
            if(maps[i][j] === ' ' && m == 1) maps[i][j] = '#';
        })
    })
    const changeMap = maps.map((m) => {
        return m.join('');
    })
    
    return changeMap;
}