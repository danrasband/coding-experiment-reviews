function solution(S) {
    if (!S) {
        return 0;
    }

    const numbers = S.split(',');
    const integers = numbers.map(i => parseInt(i, 10));
    return integers.reduce((a, e) => a + e, 0);
}
