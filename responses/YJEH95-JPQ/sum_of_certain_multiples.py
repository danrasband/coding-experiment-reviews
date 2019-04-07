# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    tmp = []
    for x in range(x-1, 2, -1):
        if x % 3 == 0 and x % 5 == 0:
            continue

        if x % 3 == 0 or x % 5 == 0:
            tmp.append(x)

    return sum(tmp)
