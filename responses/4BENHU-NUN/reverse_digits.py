# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    z = ''

    y = str(abs(X))
    for i in y:
        z = i+z

    ans = abs(int(z))

    if X < 0:
        ans = -1*ans

    return (ans)
