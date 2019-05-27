# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python
    if len(A) == 0:
        return ''
    prefix = ''
    for max_len in range(max([len(x) for x in A])):
        prefix_test = A[0][0:max_len+1]
        for x in A:
            if x[0:max_len+1] != prefix_test:
                return prefix
        prefix = prefix_test
    