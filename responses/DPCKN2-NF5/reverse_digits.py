# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    
    strVal = str(X)
    strLen = len(strVal)
    finalStr = ""
    firstTagisNegative = False
    for index, oneStr in enumerate(strVal):
        if oneStr == "-":
            firstTagisNegative = True
            continue            
        elif (index == strLen - 1) & (oneStr == "0"):
            continue
        else:
            finalStr = oneStr + finalStr
    if firstTagisNegative is True:
        finalStr = "-"+finalStr
    finalInt = int(finalStr)
    
    return finalInt


    
    
    