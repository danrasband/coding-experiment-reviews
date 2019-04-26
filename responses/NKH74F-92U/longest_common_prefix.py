# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, B):
    if X == 0 or X > len(B) or len(B) == 0:
        return 0
    else:
        max_product = 0
        for i in range(X-1, len(B)):
            product = 1
            for j in range(X):
                product *= B[i-j]
            if product > max_product:
                max_product = product
        return max_product
