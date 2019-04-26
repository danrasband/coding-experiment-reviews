# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(X):
    rem=0
    rev=0
    i=0
    while(X):
        rem =  X%10
        rev= (rev*10) + rem
        X=X//10
        i+=1
    print (rev)

   
  
solution(-50)