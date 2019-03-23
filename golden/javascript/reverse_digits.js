function solution(X) {
    const sign = X < 0 ? -1 : 1;
    X = Math.abs(X);
    let digits = X.toString();
    let reversedDigits = [];

    for (let i = digits.length - 1; i >= 0; i--) {
        reversedDigits.push(digits[i]);
    }

    const reversedInt = parseInt(reversedDigits.join(''), 10);
    return reversedInt * sign;
}
