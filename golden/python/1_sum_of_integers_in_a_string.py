from functools import reduce

def solution(S):
    if len(S) == 0:
        return 0

    numbers = S.split(',')
    integers = [int(i) for i in numbers]

    return reduce((lambda x, y: x + y), integers)
