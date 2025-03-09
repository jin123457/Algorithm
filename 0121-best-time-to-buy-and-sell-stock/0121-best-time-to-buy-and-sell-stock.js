var maxProfit = function (prices) {
    let buyPrice = Number.MAX_SAFE_INTEGER;
    let sellPrice = 0;
    prices.forEach((price) => {
        buyPrice = Math.min(buyPrice, price);
        sellPrice = Math.max(sellPrice, price - buyPrice);
    });

    return sellPrice;
};