# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, B):
    # write your code in Python
    if len(B) == 0 or X > len(B):
        return 0
    else:
        product = 0
        for i in range(len(B)-X+1):
            slice_ = B[i:i+X]
            slice_prod = B[i]
            for j in range(i+1, i+X):
                slice_prod = slice_prod * B[j]

            if slice_prod > product:
                product = slice_prod
        return product