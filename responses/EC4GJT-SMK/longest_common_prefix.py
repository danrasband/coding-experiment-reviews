# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python
    print(A[0][:2])
    B = len(A[0])
    print(B)
    for i in range(B):
        key_string = A[0][0:B-i]
        for string in A:
            if string = key_string:
                print(string)
    pass
