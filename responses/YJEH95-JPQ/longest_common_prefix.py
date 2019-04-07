# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if not len(A):
        return ""

    tmp = []
    for item in A[1:]:
        first = A[0]
        while len(first) > 0:
            if first in item:
                tmp.append(first)
                break
            else:
                first = first[:-1]


    if tmp == []:
        return ""
