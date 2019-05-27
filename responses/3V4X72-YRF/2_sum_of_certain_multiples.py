# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    # write your code in Python
    num=x-1
    listnum=[]
    while num>0:
        if divmod(num,15)[1]>0:
            if divmod(num,3)[1] ==0:
                listnum.append(num)
            elif divmod(num,5)[1] ==0:
                listnum.append(num)
            num=num-1
        else:
            num = num - 5
    return sum(listnum)
