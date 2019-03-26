# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    count_3 = (x - 1) // 3
    count_5 = (x - 1) // 5

    sum_set = set()

    for i in range(1, count_3+1):
        sum_set.add(i * 3)

    for i in range(1, count_5+1):
        if i % 3 == 0:
            continue
        else:
            sum_set.add(i * 5)

    return sum(sum_set)
