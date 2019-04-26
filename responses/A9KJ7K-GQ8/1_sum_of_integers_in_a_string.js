// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(S) {
    return S.split(',').reduce((acc, val) => { return parseInt(val) + parseInt(acc); })
}