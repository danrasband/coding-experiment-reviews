def solution(X):
    strValue = str(X)
    newStr = []
    isNegative = strValue[0] == '-'
    if isNegative:
        strValue = strValue[1:]
    for i in range(len(strValue) - 1, -1, -1):
        newStr.append(strValue[i])
    newStr = ''.join(newStr)
    if isNegative:
        newStr = '-' + newStr
    newVal = int(newStr)
    return newVal