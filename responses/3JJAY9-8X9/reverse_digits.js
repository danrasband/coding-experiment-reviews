// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(x) {
    var stringX=x.toString();
    var solution="";
    var size=stringX.length;
    for(var i=0;i<size;i++){
        solution+=stringX[size-i-1];
    }
    var tmp = parseInt(solution);
    if(stringX[0]=='-'){
        return 0-tmp;
    } 
    else{
        return tmp;
    }
}