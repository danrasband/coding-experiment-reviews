# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, B):
    if X > len(B) or B == []:
        return 0
    
    prod_arr = []
    for i in range(X):
        prod_arr.append(max(B))
        B.remove(max(B))
    
    product = 1 
    for number in prod_arr:
        product *= number
        
    return product
        
        