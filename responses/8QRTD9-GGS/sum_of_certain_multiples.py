# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    # write your code in Python
    N = []

    sum = 0

    for i in range(len(N)):
        if N[i] < x:
            num= N[i]
            if num % 5 == 0 and num != 5 and num != 3:
                sum += num
    return sum
