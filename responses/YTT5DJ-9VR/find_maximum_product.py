# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if len(A)==0:
        return ""
    
    pref = A[0]
    for s in A:
        while pref != s[:len(pref)]:
            pref = pref[:-1]
            #if len(pref)==0:
            #    return ""
    return pref
    pass