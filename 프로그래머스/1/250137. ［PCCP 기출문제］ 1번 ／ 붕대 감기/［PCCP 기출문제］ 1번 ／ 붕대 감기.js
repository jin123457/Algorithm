function solution(bandage, health, attacks) {
    const MAX_CONTINUOUS = bandage[0];
    const TIME_HEALTH = bandage[1];
    const CONTINUOUS_HEALTH = bandage[2];
    const LAST_ATTACK_TIME = attacks[attacks.length - 1][0];
    let max_health = health;
    let continuous_time = 0;

    for (let i = 1; i <= LAST_ATTACK_TIME; i++) {
      if (attacks[0][0] == i) {
        health -= attacks[0][1];
        attacks.shift();
        continuous_time = 0;
        if (health <= 0) {
          health = -1;
          break;
        }
      } else {
        continuous_time++;
        if (continuous_time == MAX_CONTINUOUS) {
          health += CONTINUOUS_HEALTH + TIME_HEALTH;
          continuous_time = 0;
        } else {
          health += TIME_HEALTH;
        }

        if (max_health <= health) {
          health = max_health;
        }
      }
    }
    return health;
}