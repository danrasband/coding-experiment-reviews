def solution(A):
    pref_confirmed = ''
    pref_status = True
    pref = ''
    maxlen = len(max(A, key=len))
    

    while len(pref_confirmed) < maxlen:
        pref_status = True
        pref += A[0][0]
        for i in A:
            if not i.startswith(pref):
                pref_status = False
                break
        if pref_status:
            pref_confirmed = pref
        else:
            break
    
    return pref_confirmed