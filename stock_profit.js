var timeline = [5,6,10,1,8,];
var timeline = [5,6,10,1,8,10,12,3,5,7];

var min_price = timeline[0];
var max_profit = 0;

// ECMAScript 5
timeline.forEach(function (item, index, array) {
    if (item < min_price) {
        min_price = item;
    }
    if (item > min_price) {
        if (item - min_price > max_profit) {
            max_profit = item - min_price;
            console.log("max profit: " + max_profit);
        }
    }
});
// console.log(min_price);
