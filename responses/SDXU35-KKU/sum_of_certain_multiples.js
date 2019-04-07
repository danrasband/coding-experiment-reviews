// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

const sum = (val, next) => val + next;

function solution(x) {
    let numbers = [];

    for (let i=1; i < x; i++) {
        if (i % 3 === 0) {
            if (i % 5 !== 0) {
                numbers.push(i);
            }
        } else if (i % 5 === 0) {
            numbers.push(i);
        }
    }

    return numbers.reduce(sum);
}
