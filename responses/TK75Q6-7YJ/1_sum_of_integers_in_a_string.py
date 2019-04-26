def solution(S):
    numbers = S.split(",")
    result = sum(int(i) for i in numbers)
    return result