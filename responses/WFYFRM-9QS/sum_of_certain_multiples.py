# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    # write your code in Python]
    if x is not None:
        if x < 3:
            return 0
        elif x == 4:
            return 3
        elif x ==5:
            return 3
        else:
            numList3 = [num for num in range(3, x, 3)]
            numList5 = [num for num in range(5, x, 5)]
            numSet3 = set(numList3)
            numSet5 = set(numList5)
            bothSet = numSet3 | numSet5 # all elements in either
            minusSet = numSet3 & numSet5 # common ones are multiples of both
            endSet = bothSet - minusSet # remove multiples of both
            endSum = sum(endSet)
            return endSum
