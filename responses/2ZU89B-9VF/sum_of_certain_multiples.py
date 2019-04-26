def solution(X):

    # write your code in Python
    digitList = []
    invList =[]
    
    if X < 0:
        s = str(X)[1:]
    else:
        s = str(X)

    
    for elem in s:
        digitList.append(elem)
    
    for elem in digitList[-1::-1]:
        invList.append(elem)
 
    invStr = ''
    for elem in invList:
        invStr +=elem

    invNum = int(invStr)
    
    if X < 0:
        invNum = - invNum
        
    return invNum