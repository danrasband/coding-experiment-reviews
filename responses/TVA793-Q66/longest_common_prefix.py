def solution(X, B):
    if len(B) == 0 or X > len(B):
        return 0
    
    maxProduct = 0
    for i in range(len(B) - X + 1):
        product = 1
        for j in range(i, i + X):
            product *= B[j]
            
        if product > maxProduct:
            maxProduct = product
    
    return maxProduct