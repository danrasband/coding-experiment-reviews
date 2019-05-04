def solution(X):
    sign = 1
    if X < 0:
        sign = -1

    X = abs(X)
    digits = list(str(X))
    digits.reverse()
    digits = ''.join(digits)

    return int(digits) * sign
