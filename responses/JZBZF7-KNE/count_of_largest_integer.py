# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    number_of_items = len(A)

    if number_of_items > 0:
        max_item = max(A)
        count_item = A.count(max_item)
        return count_item
    else:
        return 0
