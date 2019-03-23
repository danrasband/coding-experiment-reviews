function solution(X, B) {
    const N = B.length;
    if (N === 0) {
        return 0;
    }
    if (N < X) {
        return 0;
    }
    if (N === 1) {
        return B[0];
    }

    var max = 0;

    for (var i = X; i <= N; i++) {
        var range = B.slice(i - X, i);
        var prod = range.reduce(((a, e) => a * e), 1);
        if (prod > max) {
            max = prod;
        }
    }

    return max;
}
