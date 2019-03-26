// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
    // write your code in JavaScript
    if(A.lenght==0) return 0;
    var heightestNumber =-100000;
    var count=0;
    for(var i=0; i<A.length; i++){
        if(heightestNumber<A[i])
            heightestNumber = A[i];
    }
    for(var j=0; j<A.length; j++){
     if(A[j]==heightestNumber) count++;
    }

    return count;
}
