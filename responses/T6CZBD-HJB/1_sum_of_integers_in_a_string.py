# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    elements = S.split(',')
    output = 0
    for element in elements:
        if len(element) >= 2  and element[0] == '+':
            output += int(element[1:])
        elif len(element) >= 2 and element[0] == '-':
            output -= int(element[1:])
        elif len(element) == 1:
            output += int(element)
        
    return output