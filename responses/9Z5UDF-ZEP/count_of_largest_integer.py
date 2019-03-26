# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python
    dict1={}

    if A.shape[0] == 0:
        return 0

    for ele in A:
        if ele in dict1.keys():
            dict1[ele]=dict1[ele]+1
        else:
            dict1[ele]=1

    print(dict1)

    v=list(dict1.values())
    k=list(dict1.keys())

    return k[v.index(max(v))]
