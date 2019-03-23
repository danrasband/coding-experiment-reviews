// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
    var maxEle=A[0];
    var count =1;
    var size=A.length;
    for(var i=1;i<size;i++){
        if(A[i]>maxEle){
            maxEle=A[i];
            count = 1;
        }
        else if(A[i]==maxEle){
            count++;
        }
    }
    if(size>0){
        return count;
    }
    else{
        return 0;
    }

}
