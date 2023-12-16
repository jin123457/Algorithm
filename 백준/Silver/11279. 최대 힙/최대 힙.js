const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let [n, ...input] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const heap = [0];
const result = [];

const deleteHeap = () => {
  //heap이 빈칸일 때 result 배열의 0을 입력
  if (heap.length == 1) return 0;
  if (heap.length == 2) return heap.pop();

  //힙에서 제일 큰 수를 result 배열에 넣기
  const maxInHeap = heap[1];
  //heap의 루트를 삭제 후 마지막 요소가 루트의 자리로 이동
  heap[1] = heap.pop();
  //heap의 루트가 자식 요소보다 작을 경우 비교하면서 아래로 내려간다.
  for (let i = 1; i < heap.length; ) {
    const leftChild = i * 2;
    const rightChild = i * 2 + 1;

    let target = i;
    if (leftChild > heap.length - 1) break;
    else if (rightChild > heap.length - 1) target = leftChild;
    else target = heap[leftChild] > heap[rightChild] ? leftChild : rightChild;

    if (heap[i] < heap[target]) {
      [heap[i], heap[target]] = [heap[target], heap[i]];
      i = target;
    } else {
      break;
    }
  }
  return maxInHeap;
};

const insertHeap = (target) => {
  heap.push(target);
  for (let i = heap.length - 1; i > 1; i = Math.floor(i / 2)) {
    let parentNode = Math.floor(i / 2);
    if (heap[parentNode] < heap[i])
      [heap[i], heap[parentNode]] = [heap[parentNode], heap[i]];
    else break;
  }
};

input.map((item) => {
  if (item == 0) {
    result.push(deleteHeap(parseInt(item)));
  } else {
    insertHeap(parseInt(item));
  }
});

console.log(result.join("\n"));
