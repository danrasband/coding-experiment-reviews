# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    string_X = str(X)
    if string_X[0] == '-':
        sign = '-'
        unsigned_X = string_X[1:]
        new_X = int(''.join(sign + unsigned_X[::-1]))
    else:
        sign = ''
        new_X = int(''.join(sign + string_X[::-1]))
    return new_X