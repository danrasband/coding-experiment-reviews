# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    # write your code in Python
    ans = list(range(0,x))
    new_list = [i for i in ans if (i % 3 == 0) | (i % 5 == 0) & (i % 15 != 0)]
    return sum(new_list)
    pass