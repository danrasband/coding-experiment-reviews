# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    str_x = str(X)

    str_x.rstrip('0')

    array_x = list(str_x)

    # for x in arrat_x:

    if array_x[0] == '-':
        is_negative = True
    else:
        is_negative = False

    if is_negative:
        array_x.pop(0)

    array_x.reverse()

    if is_negative:
        result = '-' + ''.join(array_x)
    else:
        result = ''.join(array_x)

    return int(result)
