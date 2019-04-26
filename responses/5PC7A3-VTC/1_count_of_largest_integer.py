# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python
    num_dict = dict()
    for ele in A:
        if ele not in num_dict.keys():
            num_dict[ele] = 1
        else:
            num_dict[ele] += 1
    
    return num_dict[max(num_dict.keys())]