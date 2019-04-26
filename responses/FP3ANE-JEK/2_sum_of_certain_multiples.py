# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    # write your code in Python
    i = 1
    listOF = []
    while i<=x:
        print (i)
        print ("QQQQ"+str(i%3))
        if i%3==0 or i%5==0:
            print ("kkk"+ str(i))
            if i != 3 and i != 5:
                print ("qqqq"+ str(i))
                listOF.append(i)
        i = i +1
    print (listOF)
    return (sum(listOF))