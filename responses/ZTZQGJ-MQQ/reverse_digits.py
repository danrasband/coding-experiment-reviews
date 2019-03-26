# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    digits = []
    a = False
    if X<0:
        X*=-1
        a = True
    while X>0:
        digits.append(X%10)
        X=int(X/10)


    ret = 0
    for i in range(len(digits)):
        ret*=10
        ret+=digits[i]
    if a:
        ret*=-1
    return ret
    pass
