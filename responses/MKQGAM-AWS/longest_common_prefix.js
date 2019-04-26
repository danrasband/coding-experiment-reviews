// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(X, B) {
    var counter=X;
    var solution=1;
    var tmpProduct=1;
    if(B.length<=0){return 0;}
    if(X>B.length){return 0;}
    for(var i=0;i<B.length;i++){
        if(counter>0){
            tmpProduct*=B[i];
            counter--;
        }
        else{
            tmpProduct*=B[i];
            tmpProduct/=B[i-X];
        }
        if(tmpProduct>solution){
            solution=tmpProduct;
        }
    }
    return solution;
}