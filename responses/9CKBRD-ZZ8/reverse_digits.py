# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    multiples_of_3 = {}
    multiples_of_5 = {}
    to_be_added = []
    for i in range(x):
        if i % 5 == 0:
            multiples_of_5[i] = ""
        if i % 3 == 0:
            multiples_of_3[i] = ""
            
    for multiple in multiples_of_5:
        if multiple not in multiples_of_3:
            to_be_added.append(multiple)
    
    for multiple in multiples_of_3:
        if multiple not in multiples_of_5:
            to_be_added.append(multiple)
    
    total = 0
    for num in to_be_added:
        total += num
    
    return total