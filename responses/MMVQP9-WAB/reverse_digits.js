// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(x) {
    var sum = 0;
    for (var a = 0; a < x; a ++) {
        if ((a % 3 == 0) && (a % 5 != 0)) {
            sum += a;
        }  else if ((a % 3 != 0) && (a % 5 == 0)) {
            sum += a;
        } 
    }
    return sum;
}