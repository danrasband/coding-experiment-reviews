def solution(A):
    if len(A) == 0:
        return 0
    maxValue = max(A)
    return A.count(maxValue)