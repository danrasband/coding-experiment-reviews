// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(S) {
    var sum=0;
    for(var i=0;i<S.length;i++){
        if(S[i]=='-'){
            sum-=parseInt(S[i+1]);
        }
        else if(S[i]=='+'){
            sum+=parseInt(S[i+1]);
        }
    }
    return sum;
}