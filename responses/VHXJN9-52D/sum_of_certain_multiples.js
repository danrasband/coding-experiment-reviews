// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(n) {
    // write your code in JavaScript
        var sign= (n<0)? "-":"";
        n = n + "";
	return parseInt(sign+n.split("").reverse().join(""));
}