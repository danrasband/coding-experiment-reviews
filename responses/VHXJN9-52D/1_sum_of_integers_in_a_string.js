// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(S) {
    var numbersArray = S.split(',');
    var sum =0;
    for(var i=0; i<numbersArray.length; i++){
        sum+=parseInt(numbersArray[i]);
     }
return sum;
}