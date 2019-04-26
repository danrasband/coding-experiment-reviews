# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python
    string = A[0]
    length = len(string)
    for i in range(1, len(A)):
        #current_str = A[i]
        for j in range(length, -1, -1):
            if string[:j] == A[i][:j]:
                break
            else: length -=1
    return string[:length]
    