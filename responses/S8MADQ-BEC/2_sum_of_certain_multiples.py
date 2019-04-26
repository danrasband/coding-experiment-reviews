# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    # write your code in Python
    st=''
    neg=False
    if x<0:
        neg=True
        st=str(x)[1:]
    else:
        st=str(x)
        
    li= list(st)
    li.reverse()
    
    num = int(''.join(li))
    
    if neg:
        return -num
    else:
        return num