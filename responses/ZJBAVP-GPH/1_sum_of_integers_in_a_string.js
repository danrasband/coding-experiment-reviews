// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
    var max;
    var count = 0;
    
    for (var i=0; i<A.length; i++) {
        if (max === undefined) {
            max = A[i];
        } else {
            max = Math.max(max, A[i]);
        }
    }
    
    for (var j=0; j<A.length; j++) {
        if (A[j] === max) {
            count++;
        }
    }
    
    return count;
}