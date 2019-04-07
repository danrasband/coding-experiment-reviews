// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

const sortByLength = (a, b) => a.length - b.length;

function solution(A) {
    let prefix = '';
    let sortedWords = A.sort(sortByLength);

    for (let i = sortedWords[0].length; i > 0; i--) {
        const testVal = sortedWords[0].substring(0, i);
        let test = true;
        for (word of A) {
            if (word.indexOf(testVal) !== 0) {
                test = false;
            }
        }
        if (test) {
            prefix = testVal;
            break;
        }
    }

    return prefix;
}
