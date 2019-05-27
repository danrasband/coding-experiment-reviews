// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(X, B) {
    // write your code in JavaScript
    var max = 0;
    for (var i = 0; i < B.length; i++) {
        var prod = B[i];
        for (var j = i; j < X; j++) {
            console.log(prod, "*", B[j]);
            if (j < B.length) {
                prod *= B[j];
            }
        }
        if (prod > max) {
            max = prod;
        }
    }
    return max;
}