# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python
    min_word_len = min([len(x) for x in A])
    if min_word_len == 0:
        return ''

    prefix = ''
    for i in range(min_word_len):
        test = [A[0][i] == x[i] for x in A]
        if sum(test) == len(test):
            prefix += A[0][i]
        else:
            return prefix
    