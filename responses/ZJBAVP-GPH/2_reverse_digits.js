// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(X) {
    var digits = [];
    var reverse = 0;
    var negative = false;
    
    if (X < 0) {
        negative = true;
        X = Math.abs(X);
    }
    
    while (X > 0) {
        digits.push(X % 10);
        X = Math.floor(X / 10);
    }
    
    for (i=0; i<digits.length; i++) {
        var mult = Math.pow(10, (digits.length - (i + 1)));
        reverse += mult * digits[i];
    }
    
    if (negative) {
        reverse = -1 * reverse;
    }
    
    return reverse;
}