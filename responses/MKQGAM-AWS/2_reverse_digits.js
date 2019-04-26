// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(x) {
    var sum=0;
   for(var i=0;i<x;i++){
       if(i%3==0 && i%5==0){
       }
       else if(i%3==0){
           sum+=i;
       }
       else if(i%5==0){
           sum+=i;
       }
   }
   return sum;
}