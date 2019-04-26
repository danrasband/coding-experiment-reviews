// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(S) {
    // write your code in JavaScript
    
    var splitArray = S.split(",")
    
    var sum = 0
    
    for(i = 0; i < splitArray.length; i++) {
        sum = sum + parseInt(splitArray[i])
    }
    
    return sum
}