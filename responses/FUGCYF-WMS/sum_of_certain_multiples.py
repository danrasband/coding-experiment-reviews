# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    # write your code in Python
    str_x = str(X)
    new_str = ''
    negative_flag = 1
    for ch in str_x:
        if ch == '-':
            negative_flag = -1
        else:
            new_str = ch + new_str
    return int(new_str)*negative_flag