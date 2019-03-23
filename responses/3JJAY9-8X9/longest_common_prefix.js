// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
    var shortestL=A[0].length;
    var tmp=0;
    var size=A.length;
    var LCP="";
    var shortestString=A[0];
    for(var i=1;i<size;i++){
       tmp=A[i].length;
       if(tmp<shortestL){
           shortestL=tmp;
           shortestString=A[i];
       }
   }
   var cc= true;
   for(var i=0;i<shortestL;i++){
       for(var j=0;j<size;j++){
            if(shortestString[i]==A[j][i]){}
            else{
                cc=false;
                break;
            }
       }
       if(cc==false){break;}
       else{
           LCP+=shortestString[i];
       }
   }
   return LCP;
}
