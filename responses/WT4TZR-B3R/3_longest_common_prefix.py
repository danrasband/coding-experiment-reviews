# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    firstElement = A[0]
    maxStringLength = len(firstElement)
    for elements in A:
        beginLength = 1
        while (beginLength <= maxStringLength):
            if(str(firstElement[0:beginLength]) != str(elements[0:beginLength])):
                print(beginLength)
                beginLength = beginLength + 1
                output = firstElement[0:beginLength]
                break
            else:
                output = ""
                break
    return output