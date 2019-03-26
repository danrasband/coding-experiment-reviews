# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, B):
    # write your code in Python
    c = X
    p = 1
    for a in range(c):
        p = p * B[a]

    for b in range(c,len(B)):

        if B[b] > B[b-X]:
            #print(B[b] , B[b-X],p)
            p = int((p / B[b-X]) * B[b])

    return p
