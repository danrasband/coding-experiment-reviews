# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    d = dict()
    for word in A:
        word = word
        d[word] = d.get(word, 1) + 1