// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
    var terms = A.length;
    var match = 1;
    var prefix = "";
    while (match == 1) {
        for (var c = 0; c < 100; c++) {
            for (var i = 0; i < terms-1; i++) {
                if (A[i][c] != A[i+1][c]) {
                    match = 0 
                }
            }            
        }
    }
    return prefix;
}