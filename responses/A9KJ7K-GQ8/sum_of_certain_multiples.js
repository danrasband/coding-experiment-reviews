// NOTE: The question's examples include 3 and 5 in the sum,
// but specify not to include 3 and 5.

function solution(x) {
    let sum = 0;
    for (let i = 1; i < x; i++) {
        if (i % 3 === 0 || i % 5 === 0) {
            sum += i;
        }
    }
    return sum;
}
