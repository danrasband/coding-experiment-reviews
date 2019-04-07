# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    total = 0
    for i in range(x):
        if i == 0:
            continue
        elif (i % 3 == 0 and i != 3):
            total = total + i
            continue
        elif (i % 5 == 0 and i != 5):
            total = total + i
            continue
    return total
    # Confused and not sure what the question is really asking for
