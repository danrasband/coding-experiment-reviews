# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python
    for val in A:
        strv = strv + myFunc(val)
    
    return strv


def myFunc(arrayVal):
    for strVal in arrayVal:
        firstChar = strVal[0]
        if firstChar in valueStore:
            valueStore[firstChar].append(strVal[1:])
        else:
            valueStore[firstChar] = [strVal[1:]]
            
    cnt = 1
    for key, newStrList in valueStore:
        if len(newStrList) > cnt:
            cnt = len(newStrList)
            retStr = key
            retVal = newStrList
    
    return d[key] = retVal