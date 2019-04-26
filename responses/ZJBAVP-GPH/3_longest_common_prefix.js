// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(X, B) {
    var max = 0;
    
    if (X > B.length) {
        return max;
    }

    for (var i=0; i<(B.length - X), i++) {
        sum = 0;
        for (j=0, j<X, j++) {
            sum += B[j];
        }
        max = Math.max(max)
    }
      
}