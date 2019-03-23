from functools import reduce

def solution(x):
    match = lambda i: (i % 3 == 0 or i % 5 == 0) and i % 15 != 0
    integers = [i for i in range(x) if match(i)]
    if len(integers) == 0:
        return 0

    return reduce((lambda m, i: m + i), integers)
