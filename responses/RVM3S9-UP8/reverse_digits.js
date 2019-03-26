// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(X) {
    // write your code in JavaScript
    X_str = X.toString();
    X_str_reverse = X_str.split("").reverse().join("");
    X_reverse = parseInt(X_str_reverse);
    return X_reverse
}
