const readLine = require('fs').readFileSync('dev/stdin').toString().trim();
const [N, ...input] = readLine.split('\n');
const answer = [];

for (let i = 0; i < input.length; i += 2) {
  const [docsCount, currentDocs] = input[i].split(' ').map((number) => Number(number));
  const docsQueue = input[i + 1].split(' ').map((number) => Number(number));
  const myDocsLevel = docsQueue[currentDocs];

  const map = new Map();
  const levelMap = new Map();
  docsQueue.forEach((docs, i) => {
    map.set(i, docs);
    levelMap.set(docs, levelMap.has(docs) ? levelMap.get(docs) + 1 : 1);
  });
  const sortLevelMap = [...levelMap].sort((a, b) => b[0] - a[0]);
  const newMap = [...map];
  let num1 = 0;
  let find = false;
  while ([...map].length > 0) {
    if (sortLevelMap[0][0] > newMap[0][1]) {
      newMap.push(newMap.shift());
    } else {
      if (sortLevelMap[0][1] > 1) {
        sortLevelMap[0][1] -= 1;
      } else {
        sortLevelMap.shift();
      }

      const [index, num] = newMap.shift();

      num1 += 1;
      if (index === currentDocs) {
        find = true;
        break;
      }
    }

    if (find) break;
  }
  console.log(num1);
}
