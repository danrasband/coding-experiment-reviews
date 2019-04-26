# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Misread the problem statement. Thought it was looking for index, not count...

def solution(A):
    # write your code in Python
    deduped = set(A)
    # print(deduped)
    biggest = max(deduped)
    # print(biggest)
    size_a = len(A)
    i = 0
    for i in range(size_a):
        if A[i] < size_a and A[i] == biggest:
            return i
        elif i == size_a:
            return 0
        i += 1
    pass