# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python
    valueStore = {}
    for i in A:
        if i in valueStore:
            valueStore[i] += 1
        else:
            valueStore[i] = 1
    
    maxKey = max(valueStore, key=(lambda key: valueStore[key]))
    return valueStore[maxKey]