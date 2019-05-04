function solution(A) {
    if (!A.length) {
        return 0;
    }

    var maxInt = A[0];
    var count = 1;

    for (var i = 1; i < A.length; i++) {
        if (A[i] > maxInt) {
            maxInt = A[i];
            count = 1;
        }
        else if (A[i] == maxInt) {
            count += 1;
        }
    }

    return count;
}
