// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(S) {
    // write your code in JavaScript
    var lst = S.split(",");
    var prev_value = 0;
    for (i = 0;  i < lst.length; i++) {
        prev_value = parseInt(lst[i]) + prev_value;
    }
    return prev_value;
}