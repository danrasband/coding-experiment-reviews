// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

const sum = (val, next) => val + next;

function solution(S) {
    let numbers = [];
    let numStrings = S.split(',');
    
    for (number of numStrings) {
        numbers.push(parseInt(number, 10));
    }
    
    return numbers.reduce(sum);
}