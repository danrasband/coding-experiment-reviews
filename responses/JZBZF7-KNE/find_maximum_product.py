# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, B):
    sorted_b = sorted(B)
    nums = sorted_b[-X:]

    result = 1

    for num in nums:
        result = result * num

    return result
