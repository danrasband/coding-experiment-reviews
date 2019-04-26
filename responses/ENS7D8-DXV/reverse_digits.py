# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    # write your code in Python
    alist = list(range(1,x))
    #print(alist)
    blist = []
    for i in alist :
        if (i%3 == 0 or i%5 == 0) :
            if(i%3 == 0 and i%5 == 0) :
                pass
            else:
                blist.append(i)
    #print(blist, sum(blist))
    return sum(blist)
    