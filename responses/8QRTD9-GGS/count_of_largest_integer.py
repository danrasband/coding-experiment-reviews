# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python
    N = []
    N_1 = N
    counter = 0
    
    for i in range(0,len(N)):
        for j in range(0,len(N_1)):
            if N[i] == N_1[j]:
                counter += 1
    return counter