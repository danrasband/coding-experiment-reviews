// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(x) {
    // write your code in JavaScript
    var sum =0;
    for(var i=0; i<x; i++){
        if(i%15==0) continue;
        else if(i%3==0 || i%5==0){
            sum+=i;
        }
    }
    return sum;
}
