// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
    // write your code in JavaScript
    var largest_N = A[0];
    var counter = 1;
    for (i=1; i<A.length; i++){
        if (A[i]==largest_N){
            counter++;
        } else if (A[i]>largest_N){
            largest_N = A[i];
            counter = 1;
        }
    }
    return counter
}
