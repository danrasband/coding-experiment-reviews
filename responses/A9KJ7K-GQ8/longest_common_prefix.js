// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
    let done = false;
    let pos = 0;
    let prefix = "";
    let reducer = (acc, val) => {
        return acc && val.startsWith(prefix)
    }
    
    while (!done) {
        prefix += A[0][pos];
        if (A.reduce(reducer, prefix)) {
            pos += 1;   
        }
        else {
            prefix = prefix.substring(0, prefix.length - 1);
            done = true;
        }
    }
    return prefix;
}