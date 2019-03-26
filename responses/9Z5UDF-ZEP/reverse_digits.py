# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    # write your code in Python

    def reverse(s):
        if len(s) == 0:
            return s
        else:
            return reverse(s[1:]) + s[0]

    reversed = reverse(str(X)).lstrip('0')

    sign = reversed[-1]

    if sign == '-':
        reversed=int(sign+reversed[:-1])
    else:
        reversed = int(reversed)

    return reversed
