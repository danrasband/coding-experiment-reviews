# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    # write your code in Python
    q = X
    q = list(str(q))
    z = q[::-1]
    negative = False
    if ('-' in z):
        negative = True
        z.remove('-')
    k = ''.join(z)
    k = int(k)
    if negative:
        k = k * -1
    return k