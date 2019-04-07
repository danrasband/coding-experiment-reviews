# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, B):
    if (len(B) == 0) | (X > len(B)):
        return 0
    else:
        #sort the array in desc order
        B.sort(reverse=True)

        prod = 1
        for index,intVal in enumerate(B):
            if index <= X -1:
                prod = prod * intVal
            else:
                break

        return prod
