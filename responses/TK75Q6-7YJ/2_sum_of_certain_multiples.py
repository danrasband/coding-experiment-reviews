def solution(x):
    result = 0
    for i in range(3, x):
        if (i % 3 == 0 or i % 5 == 0) and i % 15 != 0:
            result += i
            
    return result