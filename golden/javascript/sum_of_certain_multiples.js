function solution(x) {
    if (x === 0) {
        return 0;
    }
    const range = [...Array(x).keys()];
    const match = (i => i % 15 !== 0 && (i % 3 == 0 || i % 5 == 0));
    const integers = range.filter(i => match(i));
    return integers.reduce(((m, i) => m + i), 0);
}
