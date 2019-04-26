// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
    // write your code in JavaScript
    if (A.length == 0) {
        return 0;
    }
    var max = 0;
    var map = {};
    for (var i = 0; i < A.length; i++) {
        var val = A[i];
        if (val > max) {
            max = val;
        }
        if (map[val]) {
            map[val] += 1;   
        }
        else {
            map[val] = 1;   
        }
    }
    return map[val];
}