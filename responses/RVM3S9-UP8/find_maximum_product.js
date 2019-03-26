// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(X, B) {
    // write your code in JavaScript
    counter = 1;
    for (i=1; i<B.length; i++) {
        if (B[i] == (B[i-1] + 1)) {
            counter++;
        } else {
            counter = 1;
        }
    }
    max_prod = X * counter;
    return max_prod
}
