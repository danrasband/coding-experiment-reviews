# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    sort_array = sorted(A, reverse=True)
    counter = 0
    for i in sort_array:
        if i == sort_array[0]:
            counter += 1
        else:
            break
    return counter