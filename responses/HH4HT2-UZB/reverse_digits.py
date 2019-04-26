# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    new_text = ''
    pos = -1
    X = str(X)
    while pos * -1 <= len(X):
        if X[pos] != '-':
            new_text = new_text + X[pos]
        else:
            new_text = '-' + new_text
        pos -=1
    return int(new_text)