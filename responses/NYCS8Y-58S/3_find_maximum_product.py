# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, B):
    if len(B) == 0:
        return 0
    if X > len(B):
        return 0
    highest_value = 0
    for b_index in range(len(B)-X+1):
        temp_total = []
        for x_index in range(X):
            temp_total.append(B[b_index+x_index])
        product_temp = 1
        for temp_total_value in temp_total:
            product_temp *= temp_total_value
        if highest_value < product_temp:
            highest_value = product_temp
    return highest_value