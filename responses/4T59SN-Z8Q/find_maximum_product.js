// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(X, B) {
    // write your code in JavaScript
    if(B.length==0 || B.length<X) return 0;

    var maxProduct=0;

    for(var i=0; i<B.length-X; i++){
           var product=1;
           for(var j=1; j<=X; j++){
               product*=B[i+j];
           }
           if(product>maxProduct) maxProduct=product;
    }
    return maxProduct;
}
