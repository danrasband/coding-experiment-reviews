

def max_pro(li,k):
    pro = 1
    for  it in li[:k]:
        pro *= it
    mx = pro

    for i in range(k,len(li)):
        pro = (pro * li[i]) // li[i-k]
        if pro > mx:
            mx=pro

    return mx

def solution(X,B):
    ans= 0

    while B:
        try:
            ind = B.index(0)
            if ind>=X:
                a = max_pro(B[:ind],X)
                if a> ans:
                    ans =a
            B=B[ind+1:]

        except:

            if len(B)>=X:
                a = max_pro(B,X)
                if a> ans:
                    ans=a
            B=[]


    return ans
