// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(X) {
    // write your code in JavaScript
    var strVal = X.toString();
    var mod = 1;
    strVal = strVal.split("").reverse().join("");
    if (X < 0) {
        mod = -1;
    }

    return parseInt(strVal) * mod;
}