// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
    // write your code in JavaScript
    
    A.sort(function(a, b) { return a - b });
    
    var highestInt = null;
    var times = 0;
    
    for(i = 0; i < A.length; i++) {
        var currentInt = A[i];
        
        if(highestInt == null || highestInt != currentInt) {
            highestInt = currentInt;
            times = 1;
        } else {
            times++;
        }
    }
    
    return times;
}