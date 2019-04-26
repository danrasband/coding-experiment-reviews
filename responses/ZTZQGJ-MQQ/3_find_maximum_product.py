# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, B):
    K = len(B)
    if K==0 or X>K:
        return 0
    
    B = sort(B)
    product = 1
    for i in B[:X]:
        product *= i
    return product
    

def sort(arr):
    swaps = 1
    while swaps>0:
        swaps = 0
        for i in range(len(arr)-1):
            if arr[i]<arr[i+1]:
                swaps += 1
                tmp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1]=tmp
                
    return arr

def argmax(arr):
    m = 0
    for i in range(len(arr)):
        
        if arr[i]>arr[m]:
            m =i
    return m