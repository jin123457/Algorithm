function solution(friends, gifts) {
    let gift_name = {};
    let gift = Array.from(Array(friends.length), () =>
      Array(friends.length).fill(0)
    );
    let gift_all = Array.from(Array(friends.length).fill(0));
    let next_gift = Array.from(Array(friends.length).fill(0));
    for (let i = 0; i < friends.length; i++) {
      gift_name[friends[i]] = i;
    }

    for (let i = 0; i < gifts.length; i++) {
      let [send, recive] = gifts[i].split(" ");
      gift[gift_name[send]][gift_name[recive]] += 1;
      gift_all[gift_name[send]] += 1;
      gift_all[gift_name[recive]] -= 1;
    }

    for (let i = 0; i < gift.length; i++) {
      for (let j = i; j < gift[i].length; j++) {
        if (i == j) continue;
        if (gift[i][j] > gift[j][i]) {
          next_gift[i] += 1;
        } else if (gift[i][j] < gift[j][i]) {
          next_gift[j] += 1;
        } else {
          if (gift_all[i] > gift_all[j]) {
            next_gift[i] += 1;
          } else if (gift_all[i] < gift_all[j]) {
            next_gift[j] += 1;
          }
        }
      }
    }
    return Math.max(...next_gift);
}