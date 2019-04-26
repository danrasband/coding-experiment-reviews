// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(X, B) {
    if(B.length == 0 || X > B.length)
        return 0
    
    var prod = 1
    
    for(i = B.length - 1; i >= B.length - X; i--) {
        prod = prod * B[i]
    }
    
    return prod
}