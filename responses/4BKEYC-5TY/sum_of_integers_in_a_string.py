# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python
    from collections import Counter
    c = Counter()
    for num in A:
        c[num] += 1
        
    return max(c.values())